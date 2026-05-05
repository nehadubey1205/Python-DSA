arr = [1,2,3,4,5]
# arr.reverse()
# print(arr)
## reverse
print(len(arr)-1)
left = 0
right = len(arr) - 1
for i in range(len(arr)-1):
    arr[left],arr[right] = arr[right],arr[left]
    left = left+1
    right = right-1
print(arr)
