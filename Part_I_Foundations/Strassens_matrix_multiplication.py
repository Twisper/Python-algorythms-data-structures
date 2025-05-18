def next_power_of_2(n):
    """
    Returns the next power of 2 close to n

    Args:
        n: integer

    Returns:
        The smallest power of 2 greater than or equal to n.
    """
    return 1 << (n - 1).bit_length()

def add_zeros(matrix):
    """
    Adds zeros to a matrix, so its size becomes power of 2

    Args:
        matrix: 2D array

    Returns:
        2D array with zeros added
    """
    size = len(matrix)
    new_size = next_power_of_2(size)
    for i in range(size):
        for j in range(size,new_size):
            matrix[i].append(0)
    for i in range(size, new_size):
        matrix.append([0 for _ in range(new_size)])
    return matrix

def arythm_matrix(a, b, a_height, a_length, b_height, b_length, size, operation):
    """
    Finds sum or difference between two matrices

    Args:
        a: 2D array (matrix)
        b: 2D array (matrix)
        a_height, a_length: coordinates of high left angle in a matrix
        b_height, b_length: coordinates of high right angle in b matrix
        size: size of matrices
        operation: operation to perform

    Returns:
        Result of operation
    """
    c = [[0 for _ in range(size)] for _ in range(size)]
    if operation == '+':
        for i in range(size):
            for j in range(size):
                c[i][j] = a[a_height+i][a_length+j] + b[b_height+i][b_length+j]
    elif operation == '-':
        for i in range(size):
            for j in range(size):
                c[i][j] = a[a_height+i][a_length+j] - b[b_height+i][b_length+j]
    return c
def strassen(a, b, a_height, a_length, b_height, b_length, size):
    """
    Finds multiplication of two matrices using Strassen's algorithm

    Args:
        a: 2D array (matrix)
        b: 2D array (matrix)
        a_height, a_length: coordinates of high left angle in a matrix
        b_height, b_length: coordinates of high right angle in b matrix
        size: size of matrices

    Returns:
        Multiplication result
    """
    if size == 1:
        return [[a[a_height][a_length] * b[b_height][b_length]]]
    else:
        s1 = arythm_matrix(b,b, b_height, b_length + size//2, b_height + size//2, b_length + size//2, size//2, '-')
        s2 = arythm_matrix(a,a, a_height, a_length, a_height, a_length + size//2, size//2, '+')
        s3 = arythm_matrix(a,a, a_height + size//2, a_length, a_height + size//2, a_length + size//2, size//2, '+')
        s4 = arythm_matrix(b,b, b_height + size//2, b_length, b_height, b_length, size//2, '-')
        s5 = arythm_matrix(a,a, a_height, a_length, a_height + size//2, a_length + size//2, size//2, '+')
        s6 = arythm_matrix(b,b, b_height, b_length, b_height + size//2, b_length + size//2, size//2, '+')
        s7 = arythm_matrix(a,a, a_height, a_length + size//2, a_height + size//2, a_length + size//2, size//2, '-')
        s8 = arythm_matrix(b,b, b_height + size//2, b_length, b_height + size//2, b_length + size//2, size//2, '+')
        s9 = arythm_matrix(a,a, a_height, a_length, a_height + size//2, a_length, size//2, '-')
        s10 = arythm_matrix(b,b, b_height, b_length, b_height, b_length + size//2, size//2, '+')
        p1 = strassen(a,s1, a_height, a_length, 0, 0, size//2)
        p2 = strassen(s2,b, 0, 0, b_height + size//2, b_length + size//2, size//2)
        p3 = strassen(s3,b, 0, 0, b_height, b_length, size//2)
        p4 = strassen(a,s4, a_height + size//2, a_length + size//2, 0, 0, size//2)
        p5 = strassen(s5,s6, 0, 0, 0, 0, size//2)
        p6 = strassen(s7,s8, 0, 0, 0, 0, size//2)
        p7 = strassen(s9,s10, 0, 0, 0, 0, size//2)
        c12 = arythm_matrix(p1,p2,0,0,0,0, size//2,'+')
        c21 = arythm_matrix(p3,p4,0,0,0,0, size//2,'+')
        sum1 = arythm_matrix(p5,p4,0,0,0,0, size//2,'+')
        sub1 = arythm_matrix(sum1,p2,0,0,0,0, size//2,'-')
        c11 = arythm_matrix(sub1,p6,0,0,0,0, size//2,'+')
        sum2 = arythm_matrix(p5,p1,0,0,0,0, size//2,'+')
        sub2 = arythm_matrix(sum2,p3,0,0,0,0, size//2,'-')
        c22 = arythm_matrix(sub2,p7,0,0,0,0, size//2,'-')
        for i in range(size//2):
            c11[i] += c12[i]
            c21[i] += c22[i]
        c = c11 + c21
        return c

def strassen_wrapper(arr1, arr2):
    """
    Wrapper function for strassen's algorithm

    Args:
        arr1: 2D array (matrix)
        arr2: 2D array (matrix)

    Returns:
        Multiplication result
    """
    if len(arr1) != next_power_of_2(len(arr1)):
        arr1 = add_zeros(arr1)
        arr2 = add_zeros(arr2)
    arr3 = strassen(arr1, arr2, 0, 0, 0, 0, len(arr1))
    res = [arr3[i][:len(arr1) - 1] for i in range(len(arr1)-1)]
    return res

if __name__ == "__main__":
    arr1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    arr2 = [[9, 8, 7], [6, 5, 4],[3, 2, 1]]
    res = strassen_wrapper(arr1, arr2)
    print(res)

#I don't wanna work with this anymore