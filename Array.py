class DynamicArray:
    def __init__(self, initial_capacity=10):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity

    def insert(self, x):
        """Amortized O(1) insertion with doubling strategy"""
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = x
        self.size += 1

    def delete(self, x):
        """O(n) deletion with quarter-capacity shrinking"""
        index = self.search(x)
        if index == -1:
            return False
            
        # Swap with last element and truncate
        self.array[index] = self.array[self.size-1]
        self.size -= 1
        
        if self.size <= self.capacity // 4:
            self._resize(self.capacity // 2)
        return True

    def search(self, x):
        """O(n) linear search"""
        for i in range(self.size):
            if self.array[i] == x:
                return i
        return -1

    def _resize(self, new_capacity):
        """O(n) resizing operation"""
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        return f"Size: {self.size}, Capacity: {self.capacity}, Elements: {self.array[:self.size]}"

# Python Usage Example
da = DynamicArray(5)
da.insert(10)
da.insert(20)
da.insert(30)
print(da)  # Size: 3, Capacity: 5

da.delete(20)
print(da)  # Size: 2, Capacity: 5

da.delete(10)
da.delete(30)
print(da)  # Size: 0, Capacity: 2 (auto-shrunk)
