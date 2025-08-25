def printer(a):
    if a==0:
        return
    print(a)
    printer(a-1)
a=int(input("Enter a number : "))
printer(a)