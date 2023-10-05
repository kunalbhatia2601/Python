# @Kunalbhatia-Hub

from math import *
from collections import *
from sys import *
from os import *


n=int(input())
for i in range(n):
    print(" "*(n-i-1),end="")
    for j in range(i+1,2*i+2):
        print(j,end="")
    for k in range(j-1,i,-1):
        print(k,end="")
    print()

# @Kunalbhatia-Hub