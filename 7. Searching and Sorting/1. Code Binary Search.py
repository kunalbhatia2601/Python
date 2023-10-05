# @Kunalbhatia-Hub

def search(nums: [int], target: int):
    l=0
    r=len(nums)-1

    while l<=r:

        mid=l+(r-l)//2

        if nums[mid]==target:
            return mid

        elif nums[mid]>target:
            r=mid-1
        
        elif nums[mid]<target:
            l=mid+1
        
    return -1


    
n= int (input())
arr = list(map(int,input().strip().split()))[:n]
target =int (input())

print(search(arr, target))

# @Kunalbhatia-Hub