def sum_cross_array(array, l, m, r):
    """
    Finds sum of cross product of array

    Args:
        array: list of integers
        l: index of left element in subarray
        m: index of middle element in subarray
        r: index of right element in subarray

    Returns:
        Tuple of three elements: left index of subarray with maximum sum, right index and sum of subarrays
    """
    left_sum = float('-inf')
    cur_sum = 0
    left_index = m
    for i in range(m, l - 1, -1):
        cur_sum += array[i]
        if left_sum < cur_sum:
            left_sum = cur_sum
            left_index = i
    right_sum = float('-inf')
    cur_sum = 0
    right_index = m + 1
    for i in range(m + 1, r + 1):
        cur_sum += array[i]
        if right_sum < cur_sum:
            right_sum = cur_sum
            right_index = i
    return left_index, right_index, left_sum + right_sum

def max_subarray(array, l, r):
    """
    Finds the maximum subarray (indices and sum) within array[l..r] using a divide and conquer approach.

    Args:
        array: list of integers
        l: index of left element in array
        r: index of right element in array

    Returns:
        A tuple (start_index, end_index, sum) representing the maximum subarray found.
    """
    if l == r:
        return l, r, array[l]
    else:
        m = (l + r) // 2
        left = max_subarray(array, l, m)
        right = max_subarray(array, m + 1, r)
        cross = sum_cross_array(array, l, m, r)
        if max(left[2], right[2], cross[2]) == cross[2]:
            return cross
        elif max(left[2], right[2], cross[2]) == left[2]:
            return left
        else:
            return right

def max_subarray_wrapper(array):
    """
    Taking an array as an input and automatically puts necessary arguments into finding max sum function

    Args:
        array: list to find max sum in subarrays

    Returns:
        maximum_subarray
    """
    if not array:
        return []
    max_sum = max_subarray(array, 0, len(array) - 1)
    return max_sum

if __name__ == "__main__":
    array = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    print(max_subarray_wrapper(array))