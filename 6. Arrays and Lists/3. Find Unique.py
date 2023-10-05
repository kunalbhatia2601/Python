# @Kunalbhatia-Hub

import sys

def findUnique(arr, n) :

    for x in range(n):
        cnt=0
        for y in range(n):
            if arr[x] == arr[y]:
                cnt=cnt+1
        if cnt==1:
            return arr[x]    




#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1

# @Kunalbhatia-Hub