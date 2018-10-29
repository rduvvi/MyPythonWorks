# Python operators used to perform operation on operands.

# Arithmetic Operators * ,/,-
x=4
y=5
print(x+y)

# Comparison Operators Likewise,you can try  (x < y, x==y, x!=y, etc.)
print(('x > y  is',x>y))

num1=5
num2=6
res = num1 + num2
res += num1
print(("Line 1 - Result of + is ", res))

# Logical Operators - AND,NOT,OR
a = True
b = False
print(('a and b is',a and b))
print(('a or b is',a or b))
print(('not a is',not a))

# Membership Operators - in, not in
x=4
y=5
list=[1,2,3,4,5];
if(x in list):
    print("x in the given list")
else:
    print("x not availble in the given list")
if(y not in list):
    print("Y is not available in the list")
else:
    print("Y in the given list")

# Identity Operators - To compare the memory location of two objects, Identity Operators are used. The two identify operators used in Python are (is, is not).

x=20
y=20
if(x is y):
    print("x & Y SAME identity")
else:
    print("x & y have DIFFERENT identity")
# Operator precedence - The operator precedence determines which operators need to be evaluated first.

v = 4
w = 5
x = 8
y = 2
z = 0
z = (v+w) * x / y;
print("Value of (v+w) * x/ y is ",  z)