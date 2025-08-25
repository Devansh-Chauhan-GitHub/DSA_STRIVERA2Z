def count(a):
    n=0
    while(a>0):
        a=a//10
        n=n+1
    return n
a=int(input("Enter the number : "))
print("The number of digits are : ",count(a))