a = list(map(int,input("enter numbers:").split()))
count = {}
for i in a:
    count[i] = count.get(i,0)+1
print(count)