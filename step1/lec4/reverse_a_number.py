def reverse(a):
    sum=0
    while(a>0):
        r=a%10
        sum=sum*10+r
        a=a//10
    return sum
a=int(input("Enter a number: "))
print(reverse(a))
