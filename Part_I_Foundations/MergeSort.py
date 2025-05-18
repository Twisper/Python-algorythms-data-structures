def merge(array, p, q, r):
    """
    Merges two subarrays into one, comparing two elements at one time and putting lowest in array

    Args:
        array: list to sort
        p: index of first element in subarray
        q: index of middle element in subarray
        r: index of last element in subarray

    No returns, function edits array without returning
    """
    L = array[p:q + 1]
    R = array[q + 1:r + 1]
    i, j = 0, 0
    L.append(float('inf'))
    R.append(float('inf'))
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1


def merge_sort(array, p, r):
    """
    Recursively sorts an array by dividing it into two halves, sorting them, and then merging them

    Args:
        array: list to sort
        p: index of first element in subarray
        r: index of last element in subarray

    Returns:
        Sorted list
    """
    if p < r:
        q = (p + r) // 2
        merge_sort(array, p, q)
        merge_sort(array, q + 1, r)
        merge(array, p, q, r)
    return array


def merge_sort_wrapper(array):
    """
    Taking an array as an input and automatically puts necessary arguments into sorting function

    Args:
        array: list to sort

    Returns:
        Sorted list
    """
    if not array:
        return []
    else:
        merge_sort(array, 0, len(array) - 1)
        return array


if __name__ == '__main__':
    array = [2, 8, 7, 1, 3, 5, 6, 4]
    sorted_array = merge_sort_wrapper(array)
    print(sorted_array)