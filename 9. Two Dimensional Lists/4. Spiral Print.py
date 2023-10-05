from sys import stdin


def helper(matrix):

    m, n = len(matrix), len(matrix[0])
    
    rmin, rmax = 0, m - 1
    cmin, cmax = 0, n - 1
    
    r, c = 0, 0
    dr, dc = 0, 1
    
    result = []
    
    for x in range(n * m):
        result.append(matrix[r][c])
        
        if c + dc > cmax:
            dr, dc = 1, 0
            rmin += 1
        elif r + dr > rmax:
            dr, dc = 0, -1
            cmax -= 1
        elif c + dc < cmin:
            dr, dc = -1, 0
            rmax -= 1
        elif r + dr < rmin:
            dr, dc = 0, 1
            cmin += 1            
        
        r, c = r + dr, c + dc
        
    return result



def spiralPrint(mat, nRows, mCols):

    # tempRow = nRows

    # if nRows%2 != 0:
    #     tempRow+=1

    # for i in range(tempRow//2):

    #     for w in range(i, mCols-i):
    #         print(mat[i][w], end=" ")

    #     for x in range(i+1, nRows-i):
    #         print(mat[x][w], end=" ")

    #     for y in range(mCols-i-2, i-1, -1):
    #         print(mat[x][y], end=" ")

    #     for z in range(nRows-i-2, i, -1):
    #         print(mat[z][y], end=" ")


    if nRows < 1:
        print()
        return

    result = helper(mat)

    for i in result:
        print(i, end=" ")



#Taking Input Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1