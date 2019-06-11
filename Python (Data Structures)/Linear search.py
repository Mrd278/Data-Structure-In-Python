# Linear Search


def ls(a, key):  # Function to check whether the element is present or not
    position = 0
    flag = False
    while position < len(a) and not flag:
        if a[position] == key:
            flag = True
        else:
            position = position+1
    return flag


# Main Function
A = []
c = int(input('Enter the length \t'))
print('Enter the Elements:')
for i in range(c):
    d = int(input())
    A.append(d)

val = int(input('Enter the value to search'))
found = ls(A, val)
if found:
    print("Element is present")
else:
    print("Not found")

