# Lecture 5 — Recursion & Basic Array Programs

This README explains the small programs in this folder (recursion-focused and one array utility). For each file we provide:

* short description
* the main idea / algorithm
* example input & output
* complexity notes
* illustrative call-stack diagrams
* code snippets

---

## Files covered

* `factorial_recursion.py`
* `fibnocci_recursion.py`
* `print_1_to_N.py`
* `print_N_to_1.py`
* `print_name_n_times.py`
* `string_palindrome.py`
* `Sum of First N Numbers.py`
* `Reverse_array.py`

---

## `factorial_recursion.py`

**Code:**

```python
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

n = int(input("Enter a number: "))
print(fact(n))
```

**Example run:**

```
Enter a number: 5
120
```

**Explanation:** Computes factorial recursively.
**Call Stack Diagram for n=5:**

```
fact(5)
 -> 5 * fact(4)
      -> 4 * fact(3)
           -> 3 * fact(2)
                -> 2 * fact(1)
                     -> 1 (base case)
```

**Complexity:** Time O(n), Space O(n) (stack)

---

## `fibnocci_recursion.py`

**Code:**

```python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

n = int(input("Enter a number: "))
print(fib(n))
```

**Example run:**

```
Enter a number: 6
8
```

**Call Stack Diagram for n=4:**

```
fib(4)
 -> fib(3) + fib(2)
    -> (fib(2) + fib(1)) + (fib(1) + fib(0))
       -> ((fib(1)+fib(0))+1) + (1+0)
```

**Complexity:** Time O(2^n), Space O(n) (stack)

---

## `print_1_to_N.py`

**Code:**

```python
def printre(a):
    if a == 0:
        return
    printre(a-1)
    print(a)

a = int(input("Enter a number: "))
printre(a)
```

**Example run:**

```
Enter a number: 5
1
2
3
4
5
```

**Call Stack Diagram for a=3:**

```
printre(3)
 -> printre(2)
      -> printre(1)
           -> printre(0) [returns]
           print(1)
      print(2)
print(3)
```

**Complexity:** Time O(n), Space O(n)

---

## `print_N_to_1.py`

**Code:**

```python
def printer(a):
    if a == 0:
        return
    print(a)
    printer(a-1)

a = int(input("Enter a number: "))
printer(a)
```

**Example run:**

```
Enter a number: 5
5
4
3
2
1
```

**Call Stack Diagram for a=3:**

```
printer(3)
 print(3)
 printer(2)
    print(2)
    printer(1)
        print(1)
        printer(0) [returns]
```

**Complexity:** Time O(n), Space O(n)

---

## `print_name_n_times.py`

**Code:**

```python
def printer(a):
    if a == 0:
        return
    printer(a-1)
    print("abc")

a = int(input("Enter a number: "))
printer(a)
```

**Example run:**

```
Enter a number: 3
abc
abc
abc
```

**Call Stack Diagram for a=3:**

```
printer(3)
 -> printer(2)
      -> printer(1)
           -> printer(0) [returns]
           print('abc')
      print('abc')
print('abc')
```

**Complexity:** Time O(n), Space O(n)

---

## `string_palindrome.py`

**Code:**

```python
def palindrome(start, end, s):
    if start > end:
        return True
    if s[start] != s[end]:
        return False
    return palindrome(start+1, end-1, s)

s = input("Enter a string: ")
print(palindrome(0, len(s)-1, s))
```

**Example run:**

```
Enter a string: radar
True
```

**Call Stack Diagram for 'radar':**

```
palindrome(0,4)
 -> palindrome(1,3)
      -> palindrome(2,2)
           -> palindrome(3,1) [returns True]
```

**Complexity:** Time O(n), Space O(n)

---

## `Sum of First N Numbers.py`

**Code:**

```python
def sum(a):
    if a == 1:
        return 1
    return a + sum(a-1)

a = int(input("Enter a number: "))
print(sum(a))
```

**Example run:**

```
Enter a number: 5
15
```

**Call Stack Diagram for a=3:**

```
sum(3)
 -> 3 + sum(2)
      -> 2 + sum(1)
           -> 1 [returns]
```

**Complexity:** Time O(n), Space O(n)

---

## `Reverse_array.py`

**Code:**

```python
def reverse(arr, n):
    start = 0
    end = n-1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

arr = [1,5,4,7,9]
n = len(arr)
print(reverse(arr, n))
```

**Example run:**

```
[9, 7, 4, 5, 1]
```

**Call Stack Diagram (illustrative step of swaps):**

```
Initial: [1,5,4,7,9]
Swap index 0 & 4 -> [9,5,4,7,1]
Swap index 1 & 3 -> [9,7,4,5,1]
Stop as start >= end
```

**Complexity:** Time O(n), Space O(1)
