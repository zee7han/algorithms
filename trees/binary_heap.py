class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def percolate_up(self,i):
        while (i//2) > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                temp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i//2

    def insert(self,k):
        self.heap_list.append(k)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)


    def min_child(self, i):
        if (i*2)+1 > self.current_size:
            return i*2
        else:
            if self.heap_list[i*2] < self.heap_list[(i*2)+1]:
                return i*2
            else:
                return (i*2)+1

    def percolate_down(self,i):
        while (i*2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[mc]
                self.heap_list[mc] = self.heap_list[i]
                self.heap_list[i] = temp
            i = mc

    def delete_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size -1
        self.heap_list.pop()
        self.percolate_down(1)
        return ret_val
