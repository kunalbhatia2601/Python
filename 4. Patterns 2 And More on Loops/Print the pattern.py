# @Kunalbhatia-Hub

n=int(input())
temp=0
k=n//2
for i in range(1,k+1,1):
    s=1+(i-1)*2*n
    temp=s
    for p in range(s,s+n,1):
        print(p,end=' ')
    print()

if(n%2==1):
    i=n//2+1
    s=1+(i-1)*2*n
    for p in range(s,s+n,1):
        print(p,end=' ')
    print()
    
r=n//2
temp+=n
for i in range(1,r+1):
    for p in range(temp,temp+n):
        print(p,end=' ')
    temp-=2*n
    print()

# @Kunalbhatia-Hub