# Selection Sort


def selection_sort(arr, length):
    max = arr[length - 1]
    for j in range(length):
        for k in range(length - j):
            if arr[k] >= max:
                max = arr[k]
                position = k
        temp = arr[length - 1 - j]
        arr[length - 1 - j] = max
        arr[position] = temp
        max = arr[length - 2 - j]


a = []
n = int(input("Enter the size of list"))
print("Enter the Elements")
for i in range(n):
    val = int(input("Element: "))
    a.append(val)
print("Unsorted List: ", a)
print("Sorting Technique Used: Selection Sort")
selection_sort(a, n)
print("Sorted list: ", a)
