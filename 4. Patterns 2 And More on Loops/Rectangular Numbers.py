# @Kunalbhatia-Hub

n=int(input())
l=n*2-1
for i in range(l):
    for j in range(l):
        mi=min(i,j)
        mi=min(mi,l-i-1)
        mi=min(mi,l-j-1)
        print(n-mi,end="")
    print()

# @Kunalbhatia-Hub