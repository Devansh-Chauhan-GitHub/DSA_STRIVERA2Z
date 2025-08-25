def armstrong(a):
    temp=a
    count=len(str(abs(a)))
    sum=0
    while(temp>0):
        r=temp%10
        sum=sum+pow(r,count)
        temp=temp//10
    if sum == a:
        return True
    else:
        return False
a=int(input("Enter the number : "))
print(armstrong(a))