s="abababaacacaqz"
hash_list=[0]*(26)
for i in s:
    hash_list[ord(i)-97]+=1
m="abcdqzA"
for i in m:
    if i >"z" or i <"a":
        print(f"{i} is 0")
    else:
        print(f"{i} is",hash_list[ord(i)-97])