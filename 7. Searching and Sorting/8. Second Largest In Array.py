# @Kunalbhatia-Hub


from sys import stdin
#MIN_VALUE = -2147483648


def secondLargestElement(arr, n):
    arr.sort()

    return arr[n-2]


def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#main
arr, n = takeInput()
print(secondLargestElement(arr, n))


# @Kunalbhatia-Hub