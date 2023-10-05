# @Kunalbhatia-Hub

n = int(input())

even=0
odd=0

while(n!=0):
    x = n%10
    if(x%2==0):
        even=even+x
    else:
        odd=odd+x
    n//=10

print(even, " ", odd)

# @Kunalbhatia-Hub