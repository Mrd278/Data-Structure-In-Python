# Insertion Sort Algorithm


def insertion_sort(arr, length):
    for i in range(1, length):
        value = arr[i]
        position = i

        while position > 0 and value < arr[position - 1]:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = value


a = []
n = int(input("Enter the size of list"))
print("Enter the Elements")
for j in range(n):
    val = int(input("Element: "))
    a.append(val)
print("Unsorted List: ", a)
print("Sorting Technique Used: Selection Sort")
insertion_sort(a, n)
print("Sorted list: ", a)
