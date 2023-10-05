# @Kunalbhatia-Hub

def merge(arr1, n, arr2, m) : 
    
    i=0
    j=0
    
    n_arr=[]

    while(i<n and j<m):
        
        if arr1[i]<arr2[j]:
            n_arr.append(arr1[i])
            i=i+1
        
        else:
            n_arr.append(arr2[j])
            j=j+1
    
    while(i<n):
        n_arr.append(arr1[i])
        i=i+1
    
    while(j<m):
        n_arr.append(arr2[j])
        j=j+1
    
    return n_arr

# @Kunalbhatia-Hub