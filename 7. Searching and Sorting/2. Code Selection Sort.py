# @Kunalbhatia-Hub

from typing import List

def selectionSort(arr: List[int]) -> None: 
    
    for i in range(len(arr)):
        
        m_i=i

        for j in range(i+1, len(arr)):
            
            if (arr[m_i] > arr[j]):
                m_i = j
        
        arr[i], arr[m_i] = arr[m_i], arr[i]

        # temp = arr[i]
        # arr[i] = arr[m_i]
        # arr[i] = temp

    return arr

# @Kunalbhatia-Hub