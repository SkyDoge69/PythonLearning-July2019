def bubbleSort(array):

    ln = len(array)
    for i in range(ln):
        for j in range(0, ln - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


array = [28, 7, 43, 12, 9, 67, 5, 30, 21]

print("Unsorted array: \n")
for x in array:
    print(x)

bubbleSort(array)

print("\nAfter sorting: \n")

for y in array:
    print(y)





















