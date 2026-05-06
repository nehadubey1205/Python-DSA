def find_missing(arr,n):
    for i in range(1,n+1):
        if i not in arr:
            return i
        
arr = [1,2,3,5]
n = 5   
missing_number = find_missing(arr,n)
print("The missing number is:", missing_number)
 
## time complexity is O(n^2) because "in" is O(n) and we are doing it for n numbers.


### 2nd methode
def missing_num(arrs,n):
    total_sum = n*(n+1)//2
    arr_sum = sum(arr)
    return total_sum - arr_sum
arrs = list(map(int,input("enter numebrs:").split()))
n = len(arrs)
missing_numb= missing_num(arrs,n)
print("The missing number is:", missing_numb)
