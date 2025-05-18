class Heap:
    """This class represents a heap"""
    def __init__(self, array):
        """
        This method initializes a heap object
        
        Args:
            array: A list that represents a heap
        """
        self.heap = array
        self.heapsize = len(array)
    def _left(self, i):
        """This method returns the left child of the ith element"""
        return 2 * i + 1
    def _right(self, i):
        """This method returns the right child of the ith element"""
        return 2 * i + 2
    def _parent(self, i):
        """This method returns the parent of the ith element"""
        return (i - 1) // 2
    def max_heapify(self, i):
        """
        Moves a node down in the tree to the right position

        Args:
            i: Index of the node to move

        Returns:
            No returns, edits heap without returning anything
        """
        l = self._left(i)
        r = self._right(i)
        if l < self.heapsize and self.heap[l] > self.heap[i]:
            largest = l
        else: largest = i
        if r < self.heapsize and self.heap[r] > self.heap[largest]:
            largest = r
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self.max_heapify(largest)
    def build_max_heap(self):
        """This method builds heap out of unsorted array using max_heapify method"""
        for i in range(self.heapsize // 2 - 1, -1, -1):
            self.max_heapify(i)
    def heap_sort(self):
        """This method builds new heap out of unsorted array, then sorts it"""
        self.build_max_heap()
        for i in range(self.heapsize, 0, -1):
            self.heap[i-1], self.heap[0] = self.heap[0], self.heap[i-1]
            self.heapsize -= 1
            self.max_heapify(0)
    def heap_maximum(self):
        """This method returns the maximum element in the heap"""
        return self.heap[0]
    def heap_extract_max(self):
        """This method extracts the maximum element from the heap"""
        if self.heapsize < 1: raise IndexError("Heap is empty")
        maximum = self.heap[0]
        self.heap[0] = self.heap[self.heapsize - 1]
        self.heapsize -= 1
        self.max_heapify(0)
        return maximum
    def heap_increase_key(self, i, key):
        """
        Increases the key of a node in the heap

        Args:
            i: Index of the node to increase
            key: Key of the node to increase

        Returns:
            No returns, edits heap without returning anything
        """
        if key < self.heap[i]: raise ValueError("New key is smaller than current key")
        self.heap[i] = key
        while i > 0 and self.heap[self._parent(i)] < self.heap[i]:
            self.heap[i], self.heap[self._parent(i)] = self.heap[self._parent(i)], self.heap[i]
            i = self._parent(i)
    def max_heap_insert(self, key):
        """
        Inserts a new node at the end of the heap

        Args:
            key: Key of the node to insert

        Returns:
            No returns, edits heap without returning anything
        """
        self.heapsize += 1
        self.heap.append(float('-inf'))
        self.heap_increase_key(self.heapsize - 1, key)

if __name__ == "__main__":
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    hs = Heap(arr)
    hs.build_max_heap()
    hs.heap_sort()
    print(hs.heap)