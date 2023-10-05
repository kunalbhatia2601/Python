# @Kunalbhatia-Hub

from os import *
from sys import *
from collections import *
from math import *

def findGcd(x, y):
    
    if y==0:
        return abs(x)
    else:
        return findGcd(y, x%y)

    pass

# @Kunalbhatia-Hub