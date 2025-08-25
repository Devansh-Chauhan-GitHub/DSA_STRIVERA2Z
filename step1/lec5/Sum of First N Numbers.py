def sum(a):
    if a == 1:
        return 1
    return a+sum(a-1)
a=int(input("Enter a number : "))
print(sum(a))