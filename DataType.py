#SEQUENCE TYPES
#indexing print(X[3]) return value
x='forg'
print(x[3]) #index
x=['pig','cow','horse']
print(x[1])
#Slicing - Substring ,Sublists,subtuples using indexes.
x='computer'
print(x[1:4]) #1-3
print(x[1:6:2]) #1,3,5
print(x[3:])#3 - end
print(x[:5]) #0 - 4
print(x[-1]) #Last item
print(x[-3:]) #Last 3 items
print(x[:-2]) #prints all expcept last 2 items

#Adding/Concatenating

x=['pig','cow']+['horse'] # List concatenation
print(x)

#muliply *
x=[8,5] * 3 #multiply List with number
print(x)

#Check membership
x=['pig','cow']+['horse']
print('horse' in x) #in or not in in a sequence

#iterating
x=[7,8,3]
for item in x: #item
    print(item*2)

#Index & item
for index, item in enumerate(x):
    print(index,item)
#number of items using len(x)

#minimum find in sequence,alpha or numeric types,but cant mix types
x='bug'
print(min(x))
x=['pig','cow']+['horse']
print(min(x))
#Maximum max(x)
#sum
x=[5,2,4,8,12]
print(sum(x))
print(sum(x[-2:]))

#Sorting - returns new list of items in sorted order and not change the original list
print(sorted(x))

#Count - retruns count of an item
x='hippo'
print(x.count('p')) # same for List
#index(item) - return index of the first occurence of item
x='hippo'
print(x.index('p'))
#Unpacking - unpack the n items into n variables
x=['pig','cow','horse']
a,b,c=x
print(a,b,c)


#Lists
#Constrrctor
x=list()
x=['a',25,'dog',8.25]
#x=list(tuple1)
#List Comprehension
x=[m for m in range(8)]
print(x)
x=[z**2 for z in range(10) if z>4]
print(x)
#resulting list:[0,1,2,3,4,5,6,7]

#delete del(x[1]) del(x)

#append - Append an sequence to a list
#x.append(99)
#extend = append an sequence to a list
w=[5,3,8,6]
k=[12,13]
w.extend(k)
print(w)
#insert to list
w.insert(1,7)
w.insert(1,['a','m'])
print(w)
#pop - pos last item off the list,and returns item

w.pop()
print(w.pop())
print(w)
#Remove - reomove first/sepcific instance of an item
w.remove(8)
print(w)

#reverse - reverse the order of the list
x.reverse()
#Sort - sort the list in place
x.sort()
""" Sorted(x) returns a new sorted list without changing the orginal list x
 x.sort()put the items of x in sorted order (sort in place)
 """