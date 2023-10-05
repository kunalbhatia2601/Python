# @Kunalbhatia-Hub

import sys

def intersections(arr1, n, arr2, m) :

    for i in range(n):
        if arr1[i] in arr2:
            print(arr1[i],end=" ")
            arr2.remove(arr1[i])



#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()

    t -= 1
    
# @Kunalbhatia-Hub