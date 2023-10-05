# @Kunalbhatia-Hub

from sys import stdin

def findTriplet(arr, n, x) :

    cnt=0

    for i in range(n):
        for j in range(i, n):
            for k in range (j, n):
                if i!=j!=k and arr[i]+arr[j]+arr[k]==x:
                    cnt+=1
    return cnt


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().strip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n



#main
t = int(stdin.readline().strip())

while t > 0 :

    arr, n = takeInput()
    x = int(stdin.readline().strip())
    print(findTriplet(arr, n, x))
    t -= 1
    
# @Kunalbhatia-Hub