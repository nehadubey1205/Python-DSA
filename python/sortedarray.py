#a = list(map(int,input("enter numebrs:").split()))
a = [1, 2, 3, 4, 5]
i = 0

while i < len(a) - 1:
    if a[i] > a[i + 1]:
        print("not sorted array")
        break
    i += 1
else:
    print("sorted array")
