# @Kunalbhatia-Hub

n=int(input())
z=1
for i in range(n,-1,-1):
    for j in range(i):
        print(z,end="")
    if z==1:
        z=0
    else:
        z=1
    print()
            
# @Kunalbhatia-Hub