import random
class QuickSort:
    """This class implements a quick sort algorithm."""
    def __init__(self, arr):
        self.arr = arr

    def _quick_sort(self, p, r):
        """
        Sorts the subarray in-place using the QuickSort algorithm.
        This version uses the last element as the pivot.

        Args:
            p: index of left element in subarray
            r: index of right element in subarray

        Returns:
            Nothing to return, edits array in-place
        """
        if p < r:
            q = self._partition(p, r)
            self._quick_sort(p, q-1)
            self._quick_sort(q+1, r)

    def _partition(self, p, r):
        """
        Chooses pivot element and partitions array into two parts, on one side elements, smaller than pivot, on another side bigger, than pivot

        Args:
            p: index of left element in subarray
            r: index of right element in subarray

        Returns:
            Index of pivot element
        """
        x = self.arr[r]
        i = p
        for j in range(p, r):
            if self.arr[j] <= x:
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                i += 1
        self.arr[i], self.arr[r] = self.arr[r], self.arr[i]
        return i

    def _random_partition(self, p, r):
        """
        Randomly chooses pivot element and partitions array into two parts, on one side elements, smaller than pivot, on another side bigger, than pivot

        Args:
            p: index of left element in subarray
            r: index of right element in subarray

        Returns:
            Index of pivot element
        """
        i = random.randint(p, r)
        self.arr[i], self.arr[r] = self.arr[r], self.arr[i]
        return self._partition(p,r)

    def _random_quick_sort(self, p, r):
        """
        Sorts the subarray in-place using the QuickSort algorithm.
        This version uses random element as the pivot.

        Args:
            p: index of left element in subarray
            r: index of right element in subarray

        Returns:
            Nothing to return, edits array in-place
        """
        if p < r:
            q = self._random_partition(p, r)
            self._random_quick_sort(p, q-1)
            self._random_quick_sort(q+1, r)
    def sort(self, use_random_pivot=False):
        """
        Sorts the subarray in-place using the QuickSort algorithm.

        Args:
            use_random_pivot (bool): if True then uses randomized pivot element else last pivot element

        Returns:
            No returns, edits array in-place
        """
        if not self.arr:
            return
        if use_random_pivot:
            self._random_quick_sort(0, len(self.arr)-1)
        else:
            self._quick_sort(0, len(self.arr)-1)
if __name__ == "__main__":
    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    qs = QuickSort(arr)
    qs.sort()
    print(qs.arr)

    arr = [2, 8, 7, 1, 3, 5, 6, 4]
    qs = QuickSort(arr)
    qs.sort(True)
    print(qs.arr)