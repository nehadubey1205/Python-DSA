z = list(map(int,input("enter the array element:").split()))
# print(z)
# y=[]
# for i in range(len(z)):
#     if z[i]!=0:
#         y.append(z[i])
    
non_zero = [i for i in z if i!=0 ]
print(non_zero)
zero = 0
for i in range(len(z)):
    if z[i]==0:
        zero = zero+1
print(non_zero+([0]*zero))
