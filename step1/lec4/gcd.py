def gcd(n1,n2):
    d=1
    for i in range(1,min(n1,n2)+1):
        if n1%i ==0  and n2%i == 0:
            d=i
    return d
n1=int(input("Enter the number n1 : "))
n2=int(input("Enter the number n2 : "))
print(gcd(n1,n2))