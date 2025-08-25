arr=[1,5,7,9,1,5,5,5,6,7]
d={}
for i in arr:
    if i not in d:
        d[i]=1
    elif i in d:
        d[i]=d[i]+1

maxcount=0
maxValue=-1
mincount=9999
minValue=9999
for key,count in d.items():
    if maxcount<count:
        maxcount=count
        maxValue=key
    if count<mincount:
        mincount=count
        minValue=key
print(f"maximum Value is {maxValue} , maximum count is {maxcount}")
print(f"minimum Value is {minValue} , minimum count is {mincount}")