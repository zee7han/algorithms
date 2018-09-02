class HashTable():

    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):

        hash_value = self.hash_function(key,len(self.slots))

        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data

        else:

            if self.slots[hash_value] == key:
                self.data[hash_value] = data

            else:
                next_slot = rehash_function(hash_value,len(self.slots))

                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = rehash_function(next_slot,len(self.slots))

                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

                else:
                    self.data[next_slot] = data


    def hash_function(self,key,size):
        return key%size

    def rehash_function(self,old_hash,size):
        return (old_hash+1)%size


    def get(self,key):

        start_slot = self.hash_function(key,len(self.slots))
        data = None
        found = False
        stop = False
        position = start_slot

        while self.slots[position] != None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]

            else:
                position = rehash_function(position,len(self.slots))

                if position == start_slot:
                    stop = True

        return data



    def __get_item__(self,key):
        return self.get(key)

    def __set_item__(self,key,data):
        return self.put(key,data)
