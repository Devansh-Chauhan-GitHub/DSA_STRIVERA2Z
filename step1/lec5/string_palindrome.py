import string
def palindrome(start,end,s):
    if start>end:
        return True
    if s[start]!=s[end]:
        return False
    return palindrome(start+1,end-1,s)
s=input("Enter a string : ")
count=len(s)
end=count-1
start=0
print(palindrome(start,end,s))