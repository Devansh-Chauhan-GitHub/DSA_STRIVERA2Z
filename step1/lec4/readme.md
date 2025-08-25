# Number Utility Programs

This README documents several basic number-based programs written in Python. Each section contains the **code**, a **detailed explanation**, and **sample output**.

---

## 1. Armstrong Number

```python
def armstrong(a):
    temp = a
    count = len(str(abs(a)))
    sum = 0
    while temp > 0:
        r = temp % 10
        sum = sum + pow(r, count)
        temp = temp // 10
    if sum == a:
        return True
    else:
        return False

a = int(input("Enter the number : "))
print(armstrong(a))
```

### Explanation

* An **Armstrong number** is a number equal to the sum of its own digits raised to the power of the number of digits.
* Example: `153 = 1³ + 5³ + 3³`

### Sample Output

```
Enter the number : 153
True
```

---

## 2. Count Digits

```python
def count(a):
    n = 0
    while a > 0:
        a = a // 10
        n = n + 1
    return n

a = int(input("Enter the number : "))
print("The number of digits are : ", count(a))
```

### Explanation

* Dividing a number repeatedly by 10 removes the last digit each time.
* The count of divisions until the number becomes 0 gives the number of digits.

### Sample Output

```
Enter the number : 12345
The number of digits are : 5
```

---

## 3. Divisors of a Number

```python
def divisors(n):
    divisor = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisor.append(i)
    return divisor

n = int(input("Enter a number : "))
print(divisors(n))
```

### Explanation

* A **divisor** of `n` is a number that divides `n` without leaving a remainder.
* We check every number from `1` to `n`.

### Sample Output

```
Enter a number : 12
[1, 2, 3, 4, 6, 12]
```

---

## 4. Greatest Common Divisor (GCD)

```python
def gcd(n1, n2):
    d = 1
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            d = i
    return d

n1 = int(input("Enter the number n1 : "))
n2 = int(input("Enter the number n2 : "))
print(gcd(n1, n2))
```

### Explanation

* The **GCD** of two numbers is the largest integer that divides both.
* We loop up to the smaller of the two numbers.

### Sample Output

```
Enter the number n1 : 20
Enter the number n2 : 28
4
```

---

## 5. Palindrome Number

```python
def palindrome(a):
    temp = a
    sum = 0
    while temp > 0:
        r = temp % 10
        sum = sum * 10 + r
        temp = temp // 10
    if sum == a:
        return True
    else:
        return False

a = int(input("Enter a number : "))
print(palindrome(a))
```

### Explanation

* A number is a **palindrome** if it reads the same forward and backward.
* Example: `121`, `1331`

### Sample Output

```
Enter a number : 121
True
```

---

## 6. Reverse a Number

```python
def reverse(a):
    sum = 0
    while a > 0:
        r = a % 10
        sum = sum * 10 + r
        a = a // 10
    return sum

a = int(input("Enter a number: "))
print(reverse(a))
```

### Explanation

* Extract each digit from the number and build a new number in reverse order.

### Sample Output

```
Enter a number: 12345
54321
```

