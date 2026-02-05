arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Bubble Sort
a = arr.copy()
for i in range(len(a)):
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Bubble Sort:", a)

# Selection Sort
a = arr.copy()
for i in range(len(a)):
    min_i = i
    for j in range(i+1, len(a)):
        if a[j] < a[min_i]:
            min_i = j
    a[i], a[min_i] = a[min_i], a[i]
print("Selection Sort:", a)

# Insertion Sort
a = arr.copy()
for i in range(1, len(a)):
    key = a[i]
    j = i - 1
    while j >= 0 and key < a[j]:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = key
print("Insertion Sort:", a)

# Radix Sort
a = arr.copy()
exp = 1
max_num = max(a)

while max_num // exp > 0:
    buckets = [[] for _ in range(10)]
    for num in a:
        buckets[(num // exp) % 10].append(num)
    a = []
    for b in buckets:
        a.extend(b)
    exp *= 10

print("Radix Sort:", a)
