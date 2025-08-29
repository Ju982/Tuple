# I. Length of Tuple without len()
def tuple_length(t):
    count = 0
    for _ in t:
        count += 1
    return count

# II. Max and Min of a Tuple
t = (5, 1, 9, 3)
print("II. Max:", max(t), "Min:", min(t))

# III. Remove Duplicates from a List
lst = [1, 2, 2, 3, 4, 4]
unique_lst = list(set(lst))
print("III. Unique List:", unique_lst)

# IV. Square Elements in a List
lst = [1, 2, 3, 4, 5]
squared = [x**2 for x in lst]
print("IV. Squared List:", squared)

# V. Merge Two Dictionaries
d1 = {'a': 1}
d2 = {'b': 2}
merged = {**d1, **d2}
print("V. Merged Dictionary:", merged)

# VI. Swap Keys and Values
d = {'a': 1, 'b': 2, 'c': 3}
swapped = {v: k for k, v in d.items()}
print("VI. Swapped Dictionary:", swapped)

# VII. Memoized Fibonacci
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print("VII. Fibonacci(10):", fib(10))

# VIII. Pythagorean Triplets
n = 30
triplets = [(a, b, c) for a in range(1, n) for b in range(a, n) for c in range(b, n) if a*a + b*b == c*c]
print("VIII. Pythagorean Triplets:", triplets)
