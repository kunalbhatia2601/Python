# @Kunalbhatia-Hub

from math import *
from collections import *
from sys import *
from os import *

n = int(input())

a=0
b=1
c=a+b

if(n==1):
    print(c)
else:
    for i in range(2,n):
        c=a+b
        a=b
        b=c
    print(c+a)


# @Kunalbhatia-Hub