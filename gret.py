"""arr=[32,98,12]
max=0
i=0
print("Original array:", arr)
for i in arr:
    if(arr[i]<arr[i+1]):
        max=arr[i+1]
print(max)"""



x=[]
num=[3,87,43]
print(num[1],num[2],num[0])
#print(num[1.0])
# print(num[1.0])  #TypeError: list indices must be integers or slices
i=0
while i<3:
    print(num[i])
    i+=1

l=[]
l.append(9)
l.append("Adarsh")
l.append(90.3)
print(l)
l.insert(0,67)
print(l)
l1=[78,93]
l.extend(l1)
print(l)
l.extend("abc")
print(l)