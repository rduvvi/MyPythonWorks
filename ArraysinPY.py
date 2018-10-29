from array import *
arr=array('i',[])

n=int(input("Enter the length of the Array"))

for i in range(n):
    x = int(input("Enter the value"))
    arr.append(x)

print(arr)

val=int(input("Enetr the number you want to search :"))
k=0
for e in arr:
    if e==val:
        print(k)
        break

    k+=1
rarr=array('i',[])
m=arr.__len__()-1

for l in range(arr.__len__()):
    rarr.append(arr[m])
    m-=1

print(rarr)