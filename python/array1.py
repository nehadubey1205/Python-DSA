arr = list(map(int,input("enter numers: ").split()))
print(arr)
maxs = arr[0]
print(maxs)
for i in arr:
    if i>maxs:
        maximum = i
print("max:",maximum)
    