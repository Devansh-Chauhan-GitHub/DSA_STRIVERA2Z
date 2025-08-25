def printre(a):
    if a==0:
        return
    printre(a-1)
    print(a)
a=int(input("Enter a number : "))
printre(a)