def CountSort(arr):
    """
    Sorts an array of integers using CountSort

    Args:
        arr: array of integers

    Returns:
        Sorted array of integers
    """
    a = max(arr)
    b = [0]*len(arr)
    c = [arr.count(i) for i in range(0,a+1)]
    for i in range(1,len(c)):
        c[i] = c[i] + c[i-1]
    for i in range(len(arr)-1,-1,-1):
        b[c[arr[i]]-1] = arr[i]
        c[arr[i]] = c[arr[i]]-1
    return b

if __name__ == '__main__':
    mas = [6,0,2,0,1,3,4,6,1,3,2]
    print(CountSort(mas))