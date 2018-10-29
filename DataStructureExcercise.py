#List in DataType

# Tuple - sequence,Immutable but members of objects may be mutable

#Constructor
x=() #no-item tuple
x=(1,2,3)
x=1,2,3 #Parenthesis are optional
#x=2,    #single-tem tuple
# x=tuple(list) tuple from list
print(x)
#immutable but member object may be mutable
x=([1,3],5)
del(x[0][1])
print(x)

#SETS
x={3,5,2,3,5}
x=set() #empty set
#x=set(list) #Set from list & Strips duplicates

#Set Comprehensiom
x={3*x for x in range(10) if x>5}
print(x) #Random Order

"""
* Basic Set Operations
Add item to set x - x.add(item)
Remove item from set x - x.remove(it)
Get length of set x - len(x)
Check memvership in x - item in x or item not in x
Pop random item from set x = x.pop()
delete all items from set x - x.clear()

*Standard Mathematical Set operations*

Set Function     Desc          Code
Intersection    AND           set1&set2
Union           OR            set1|set2
Symmentric Diff XOR           set1^set2
Difference      in set1 but not in set2    set1-set2
subset         s2contain set1   set1<=set2
SuperSet       set1 contain set2  set1>=set2

"""

#DICTIONARY - KEY VALUE PAIR

#Constructor
x={'pork':25.3,'beef':33.8,'chicken':22.7}
x=dict([('pork',25.3),('beef',33.8),('chicken',22.7)])
x=dict(pork=25.3,beef=33.8,chicken=22.7)
print(x.items())
"""
*BASIC DICTIONARY OPERATIONS*
ADD OR CHANGE ITEM IN DICT X - x['beef']=33.8
Remove item from dict x  -  del x['beef']
Get length of dict x - len(x)
Check membership in x (only looks key) - item in x or item not in x
Delete all items from dict x - del x
"""

#Accessing keys and values in a dict
# x.keys() - keys
# x.values() - values
# x.tems - returns list of key-value tuple pair in x
# item in x.vlaues - tests membership in x :returns boolean

#iterating
"""for key in x:
    print(key,x[key])"""
for k,v in x.items():
    print(k,v)

###########################################
# LAMBDA - simple ,one-time and anonymous function objects in Python.#
###########################################
mul = lambda y:y*2
print(mul(2))

add= lambda a,b:a+b
print("Add : ",add(3,5))

mx= lambda x,y:x if x>y else y
print(mx(6,8))

###########################################
# MAP -  map functions expects a function object and any number of iterables like list, dictionary, etc.
###########################################
def mult2(x):
    return x*2
print(list(map(mult2,[2,3,4,5])))
map(lambda x:x**2,[2,3,4,5])

###########################################
# Filter -  filter function expects two arguments, function_object and an iterable. function_object returns a boolean value. function_object is called for each element of the iterable and filter returns only those element for which the function_object returns true.
###########################################
a=[1,2,3,4,5]
filter_output=list(filter(lambda x:x%2==0 ,a))
print(filter_output)

###########################################
# Reduce - Applies same operation to items of sequence,use result of operation as firsr param of next operation,returns item not list
###########################################
n=[4,3,2,1]
#print(reduce())