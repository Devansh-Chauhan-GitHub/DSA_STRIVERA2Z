arr=[0,1,3,4,5,6,6,7,1,3,4,5,9]
hash_list=[0]*(max(arr)+1)
for i in arr:
    hash_list[i]+=1
m=[1,2,3,4,5,6,7,8,9,10,12]
for i in m:
    if i<0 or i>max(arr):
        print(f"{i} is ",0)
    else:
        print(f"{i} is ",hash_list[i])
