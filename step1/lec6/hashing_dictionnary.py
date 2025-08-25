arr=[1,5,10,5,1,10,7]
d={}
for i in arr:
    if i in d:
        d[i]+=1 #if already present increase by 1
    if i not in d:
        d[i]=1 #key created if element not present
for key,value in d.items():
    print(f"{key} is {value}")
