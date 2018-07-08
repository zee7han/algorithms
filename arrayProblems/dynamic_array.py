import ctypes

class DynamicArray(object):

    def __init__(self):
        self.n = 0
        self.capacity = 1
        self.A = self.makeArray(self.capacity)

# Gives the length of the array
    def __len__(self):
        return self.n

# Fetch the element of the given index
    def __getitem__(self, k):
        if not 0 <= k < self.n:
            return IndexError('K is out of bounds')
        return self.A[k]

# Appending the new element in the array
    def append(self, ele):
        if self.n == self.capacity:
            self._resize(self.capacity*2)  # double the capacity of array
        self.A[self.n] = ele
        self.n += 1

# Internal function for doubling the array size
    def _resize(self, new_cap):
        B = self.makeArray(new_cap)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.capacity = new_cap

# Create the actual new array by using the ctypes library of python
    def makeArray(self, new_cap):
        return (new_cap * ctypes.py_object)()


array = DynamicArray()
print("Initial length of the Array", len(array))
array.append(1)
array.append(2)
print("Array after appending the two element", array[0], array[1])
print("length of the Array", len(array))
print("Get element of the Array", array[0])
