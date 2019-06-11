# Binary Search

def binary_search(a, key):
    start = 0
    end = len(a)-1
    mid = int((len(a)-1)/2)
    while start < end:
        if key > a[mid]:
            start = mid + 1
        elif key < a[mid]:
            end = mid - 1
        else:
            return True
        mid = int((end + start) / 2)
    return False

# Main Function


A = []
n = int(input("Enter the length "))
print("Enter the Elements: ")
for i in range(n):
    b = int(input())
    A.append(b)
A.sort()
val = int(input("Enter the value to search"))
found = binary_search(A, val)
if found:
    print("Element found")
else:
    print("Not found")
