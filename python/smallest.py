#arr = [2,4,8,1]
arr = list(map(int, input("enter the array elements:").split()))
small = arr[0]
i =0
for i in range(len(arr)):
    if arr[i]<=small:
        small = arr[i]
        i = i+1
print(small)