# @Kunalbhatia-Hub

def findpower(x, y):
     
    if y == 0:
        return 1
    if y % 2 == 0:
        return findpower(x, y // 2) * findpower(x, y // 2)
         
    return x * findpower(x, y // 2) * findpower(x, y // 2)
 
def findorder(x):
 
    n = 0
    while (x != 0):
        n = n + 1
        x = x // 10
         
    return n
 
def isArmstrong(x):
     
    n = findorder(x)
    temp = x
    sum1 = 0
     
    while (temp != 0):
        r = temp % 10
        sum1 = sum1 + findpower(r, n)
        temp = temp // 10
 
    return (sum1 == x)

 
x = int(input())
if isArmstrong(x):
    print("true")
else:
    print("false")

# @Kunalbhatia-Hub