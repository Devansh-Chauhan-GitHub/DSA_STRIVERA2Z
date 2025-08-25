nums=[4, 4, 5, 5, 6]
hash_list=[0]*100000
for i in nums:
    hash_list[i]+=1
max_ferquency=0
req_index=9999
for i in range(len(hash_list)):
    if max_ferquency<hash_list[i]:
        max_ferquency=hash_list[i]
        req_index=i
    elif max_ferquency==hash_list[i]:
        if req_index>i:
            req_index=i
print(req_index)