arr = list(map(int,input("enter numers: ").split()))
print(arr)
maxs = arr[0]
print(maxs)
for i in arr:
    if i>maxs:
        maximum = i
print("max:",maximum)
## 2nd largest element
second_max = arr[0]
for i in arr:
    if i>second_max and i<maximum:
        second_max = i
print("2nd max:",second_max)