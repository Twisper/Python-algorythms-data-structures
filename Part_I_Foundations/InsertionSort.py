def insertion_sort(array):
    """
    Sorts an array, using insertion sort method

    Args:
        array (list): List to be sorted

    Returns:
        list: Sorted list
    """
    for i, value in enumerate(array):
        j = i - 1
        while j >= 0 and value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = value
    return array

if __name__ == "__main__":
    array = [2, 8, 7, 1, 3, 5, 6, 4]
    print(insertion_sort(array))