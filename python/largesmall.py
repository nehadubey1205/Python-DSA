arr = list(map(int,input("enter elements:").split()))
print("Array:", arr)
## largest element
large = arr[0]

for i in arr:
    if i >= large:
        large = i
print("Largest element:", large)

### smallest element
arr = list(map(int, input("Enter elements: ").split()))

small = arr[0]

for i in range(len(arr)):
    if arr[i] < small:
        small = arr[i]

print("Smallest element:", small)

## find large: above i in interation which represent element.
## find smallest: above i in index 