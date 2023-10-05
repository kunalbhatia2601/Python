# @Kunalbhatia-Hub

x=int(input())  
temp=x
check=0

while(temp>0):
    a=temp%10
    check = check*10+a
    temp=temp//10

if check == x:
    print("true")
else:
    print("false")

# @Kunalbhatia-Hub