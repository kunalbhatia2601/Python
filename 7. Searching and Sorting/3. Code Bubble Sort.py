# @Kunalbhatia-Hub

from typing import List

def bubbleSort(arr: List[int], n: int):

    for i in range(len(arr)-1):

        for j in range(len(arr)-i-1):

            if (arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# @Kunalbhatia-Hub