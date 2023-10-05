# @Kunalbhatia-Hub


from sys import stdin

def sumOfTwoArrays(arr1, m, arr2, n, output) :

    n=n-1
    m=m-1
    c=0

    x = max(m, n)+1

    while m>=0 and n>=0:
        summ = arr1[m] + arr2[n] + c

        output[x] = summ%10
        c=summ//10

        m-=1
        n-=1
        x-=1
    
    while m>=0:
        summ = arr1[m]+c

        output[x] = summ%10
        c=summ//10
        m-=1
        x-=1
    
    while n>=0:
        summ = arr2[n]+c

        output[x] = summ%10
        c=summ//10
        n-=1
        x-=1
    
    output[0] = c
        


#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0 :
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
    arr1, n = takeInput()
    arr2, m = takeInput()
    
    outputSize = (1 + max(n, m))
    output = outputSize * [0]
    
    sumOfTwoArrays(arr1, n, arr2, m, output)
    printList(output, outputSize)
    
    t -= 1


# @Kunalbhatia-Hub