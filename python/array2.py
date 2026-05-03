# arr = [1,2,4,7,3]

# left = 0
# right = len(arr) - left - 1
# print(arr[left],arr[right])
# while left<=right:
#     arr[left],arr[right]= arr[right],arr[left]
#     left = left+1
#     right = right-1

# print(arr)

arr = list(map(int,input("Enter the array elements: ").split()))

left = 0
right = len(arr) - left - 1
print(arr[left],arr[right])
while left<=right:
    arr[left],arr[right]= arr[right],arr[left]
    left = left+1
    right = right-1

print(arr)


    
    