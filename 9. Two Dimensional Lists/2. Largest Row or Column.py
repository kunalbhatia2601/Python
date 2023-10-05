from sys import stdin

def findLargest(arr, nRows, mCols):

    Rmax_sum=-2147483648
    Rmax_i=0

    Cmax_sum=-2147483648
    Cmax_i=0

    for i in range(0, nRows):

        summ=0

        for j in range(0, mCols):
            summ+=arr[i][j]
        
        if summ > Rmax_sum:
            Rmax_sum=summ
            Rmax_i=i

    
    for i in range(0, mCols):

        summ=0

        for j in range(0, nRows):
            summ+=arr[j][i]
        
        if summ > Cmax_sum:
            Cmax_sum=summ
            Cmax_i=i

    
    if Rmax_sum > Cmax_sum:
        print("row"+" " + str(Rmax_i) + " " + str(Rmax_sum))

    elif Cmax_sum > Rmax_sum:
        print("column" + " " + str(Cmax_i) + " " + str(Cmax_sum))

    else:
        print("row"+" " + str(Rmax_i) + " " + str(Rmax_sum))




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
    findLargest(mat, nRows, mCols)

    t -= 1