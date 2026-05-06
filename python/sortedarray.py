#a = list(map(int,input("enter numebrs:").split()))
a = [1, 2, 3, 4, 5]

## first method
i = 0

while i < len(a) - 1:
    if a[i] > a[i + 1]:
        print("not sorted array")
        break
    i += 1
else:
    print("sorted array")

### 2nd method
b = sorted(a)
print(b)

if a == b:
    print("here the array is sorted array")
else:    print("Array is not sorted array")
