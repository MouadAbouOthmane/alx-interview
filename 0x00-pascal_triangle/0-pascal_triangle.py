def index_exists(ls, i):
    """
    check if index is exist in array
    """
    return (0 <= i < len(ls))

def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0: return []
    arrs = [[1]]
    if n < 2: return arrs
    for i in range(n - 1):
        arr = []
        for j in range(i + 2):
            c1 = arrs[i][j - 1]  if index_exists(arrs[i], j - 1) else 0
            c2 = arrs[i][j] if index_exists(arrs[i], j) else 0
            arr.append(c1 + c2)
        arrs.append(arr)
        
    return arrs