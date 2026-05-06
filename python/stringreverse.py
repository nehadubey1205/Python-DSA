b = input("Enter a string: ")
a = list(b)

left = 0
right = len(a) - 1

while left < right:
    a[left], a[right] = a[right], a[left]
    left += 1
    right -= 1

print("Reversed string:", "".join(a))

