# @Kunalbhatia-Hub

n=int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(i,0,-1):
        print(j,end="")
    for k in range(2,i+1):
        print(k,end="")
    print()

# @Kunalbhatia-Hub