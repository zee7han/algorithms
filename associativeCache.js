class SlotSet {
    constructor(assoc, algorithm){
        this.assoc = assoc
        this.algorithm = algorithm
        this.slots = {}
        this.used = 0
    }

    STORED = 'stored'
    REPLACED = 'replaced'
    EVICTED = 'evicted'

    put(key, value) {
        let slot = new Slot(value)
        , result;
    if (this.slots[key]) {
        result = this.REPLACED;
    } else if (this.used < this.assoc) {
        this.used++;
        result = this.STORED;
    } else {
        this.algorithm.evict(this.slots);
        result = this.EVICTED;
    }
    this.slots[key] = slot;
    this.algorithm.created(slot);
    return result;
    }

    get(key) {
        let slot = this.slots[key];
        if (slot) {
            this.algorithm.accessed(slot);
            return slot.value;
        }
    }

    delete(key){
        let slot = this.slots[key];
        if (slot) {
            delete this.slots[key];
            this.used--;
        }
    }
}

class Slot {
    constructor(value) {
        this.value = value
        this.stat = {}
    }
}

class Algorithm {
    constructor(){}

    ruAccessed(slot) {
        slot.stat.accessedAt = Date.now();
    }

    fuAccessed(slot) {
        let stat = slot.stat;
        if (!stat.accessCount) stat.accessCount = 0;
        stat.accessCount++
    }

    uEvict(property, initValue, lessThan) {
        return function evict(slots) {
            let uProperty = initValue
                , uKey;
    
            for (let key in slots) {
                let stat = slots[key].stat;
                if (lessThan === stat[property] < uProperty) {
                    uProperty = stat[property];
                    uKey = key;
                }
            }
    
            delete slots[uKey];
        }
    }

    evictions = {
        lru: {
            created: this.ruAccessed,
            accessed: this.ruAccessed,
            evict: this.uEvict('accessedAt', Infinity, true)
        },
        mru: {
            created: this.ruAccessed,
            accessed: this.ruAccessed,
            evict: this.uEvict('accessedAt', -Infinity, false)
        },
        lfu: {
            created: this.fuAccessed,
            accessed: this.fuAccessed,
            evict: this.uEvict('accessCount', Infinity, true)
        },
        mfu: {
            created: this.fuAccessed,
            accessed: this.fuAccessed,
            evict: this.uEvict('accessCount', -Infinity, false)
        }
    }
}


class Cache {
    constructor(opts){
        const algo = opts.algorithm || opts.evict || 'lru'
        const algorithms = new Algorithm()
        
        this.assoc = opts.assoc
        this.size = opts.size
        this.algorithm = algorithms.evictions[algo]
        this.sets = new Array(this.size)
        this.stat = { hits: 0,misses: 0}
    }

    put(key, value) {
        key = JSON.stringify(key)
        let id = this.getSetId(key)
        let slotSet = this.sets[id]
        if (slotSet === undefined)
            slotSet = this.sets[id] = new SlotSet(this.assoc, this.algorithm)
        let result = slotSet.put(key, value)
        if (!this.stat[result]) this.stat[result] = 0
        this.stat[result]++
    }

    get(key) {
        key = JSON.stringify(key)
        let id = this.getSetId(key)
        let slotSet = this.sets[id]
        if (slotSet === undefined)
            this.stat.misses++
        else {
            let value = slotSet.get(key)
            this.stat[value === undefined ? 'misses' : 'hits']++
            return value
        }
    }

    delete(key) {
        key = JSON.stringify(key)
        let id = this.getSetId(key)
        let slotSet = this.sets[id]
        if (slotSet) slotSet.delete(key)
    }

    clear() {
        this.sets = new Array(this.size);
    }

    getSetId(key) {
        return this.dbHash(key) % this.size
    }

    dbHash(str) {
        let hash = 5381;
        for (let i = 0; i < str.length; i++) {
            let char = str.charCodeAt(i)
            hash = ((hash << 5) + hash) + char
        }
        return hash >= 0 ? hash : -hash
    }
}


let cache = new Cache({
    assoc: 4,
    size: 100
})

console.log(cache.put("abc", "yoooo"))
console.log(cache.put("xyz", "yoooo-yooooo"))
console.log(cache.put("123", "yoooo-yooooo-yoooo"))
console.log(cache.get("123"))
console.log(cache.delete("123"))
console.log(cache.get("abc"))
console.log(cache.get("xyz"))


