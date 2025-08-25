def palindrome(a):
    temp=a
    sum=0
    while(temp>0):
        r=temp%10
        sum=sum*10+r
        temp=temp//10
    if sum == a:
        return True
    else:
        return False        
a=int(input("Enter a number : "))
print(palindrome(a))