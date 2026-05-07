# arr = list(map(int,input("enter elements:").split()))
# print("Array:", arr)
# ## largest element
# large = arr[0]

# for i in arr:
#     if i >= large:
#         large = i
# print("Largest element:", large)

# ### smallest element
# arr = list(map(int, input("Enter elements: ").split()))

# small = arr[0]

# for i in range(len(arr)):
#     if arr[i] < small:
#         small = arr[i]

# print("Smallest element:", small)

# ## find large: above i in interation which represent element.
# ## find smallest: above i in index 

# ### count frequency of elements in array
# fre = {}
# for i in arr:
#     fre[i] = fre.get(i, 0) + 1

# print("Frequency of elements:", fre)


# ## palindrome
# z = "madame"
# y = z[::-1]
# print(y)

# left = 0
# right = len(z) - 1

# is_palindrome = True

# while left < right:
#     if z[left] != z[right]:
#         is_palindrome = False
#         break

#     left += 1
#     right -= 1

# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")


### move zero to end
arr = [0, 1, 0, 3, 12]

result = []

# Add non-zero elements
for num in arr:
    if num != 0:
        result.append(num)
    
z = len(arr)-len(result)
print(z)
for i in range(z):
    result.append(0)
    
print(result)


    
