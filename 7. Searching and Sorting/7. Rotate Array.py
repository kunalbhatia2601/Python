# @Kunalbhatia-Hub

from sys import stdin


def rotate(arr, n, d):

    n_ary=[]

    for i in range(d, n):
        n_ary.append(arr[i])
    for i in range(d):
        n_ary.append(arr[i])

    return n_ary




#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    arr = rotate(arr, n, d)
    printList(arr, n)
    
    t -= 1

# @Kunalbhatia-Hub