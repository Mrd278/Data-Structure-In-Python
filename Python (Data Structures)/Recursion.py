# Recursion Implementation

# Factorial using Recursion


def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

# Binary Search using Recursion


def binary_search(a, key, start, end):
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if key == a[mid]:
            return True
        elif key < a[mid]:
            return binary_search(a, key, start, mid-1)
        elif key > a[mid]:
            return binary_search(a, key, mid+1, end)
