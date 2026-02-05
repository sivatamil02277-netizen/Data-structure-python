arr = [10, 20, 30, 40, 50]
key = int(input("Enter element to search: "))

# Linear Search
for i in range(len(arr)):
    if arr[i] == key:
        print("Linear Search: Found at position", i)
        break
else:
    print("Linear Search: Not found")

# Binary Search
low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print("Binary Search: Found at position", mid)
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1
else:
    print("Binary Search: Not found")
