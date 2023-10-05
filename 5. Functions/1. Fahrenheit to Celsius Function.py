# @Kunalbhatia-Hub

import math
def printTable(s,e,w):
    for i in range(s,e+1,w):
        c=((i-32)*5)/9
        if c>0:
            x=math.floor(c)
        else:
            x=math.ceil(c)
        print(i,x,sep='\t')
	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)

# @Kunalbhatia-Hub