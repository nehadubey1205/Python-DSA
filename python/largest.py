arr = [1,6,0,3,9]
large = arr[0]
i =0
for i in range(len(arr)):
    if arr[i] >= large :
        large = arr[i]        
        i=i+1
    
print(large)
