def printer(a):
    if a == 0:
        return
    printer(a-1)
    print("abc")
a=int(input("Enter a number : "))
printer(a)