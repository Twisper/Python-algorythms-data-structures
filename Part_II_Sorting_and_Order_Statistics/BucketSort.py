import itertools
def insertion_sort(array):
    """
    Sorts an array, using insertion sort method

    Args:
        array: List to be sorted

    Returns:
        Sorted list
    """
    for i, value in enumerate(array):
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array

def bucket_sort(arr):
    """
    Sorts an array of numbers in [0;1) range using BucketSort

    Args:
        arr: array of numbers between 0 and 1

    Returns:
        Sorted array of numbers
    """
    n = len(arr)
    b = [[] for _ in range(n)]
    for element_value in arr:
        bucket_index = int(element_value * n)
        if bucket_index >= n:
            bucket_index = n - 1
        elif bucket_index < 0:
            bucket_index = 0
        b[bucket_index].append(element_value)
    for i in range(n):
        b[i] = insertion_sort(b[i])
    return list(itertools.chain.from_iterable(b))

if __name__ == "__main__":
    arr = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
    res = bucket_sort(arr)
    print(res)
