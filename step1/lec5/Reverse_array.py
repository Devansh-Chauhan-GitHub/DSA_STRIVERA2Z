def reverse(arr,n):
    start=0
    end=n-1
    while(start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
    return arr
arr=[1,5,4,7,9]
n=len(arr)
print(reverse(arr,n))