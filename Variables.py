# Declare a variable and initialize it
f=101
# Global vs. local variables in functions
def someFunction():
    f='I am learning Python'
    print(f)
def globalFunction():
    global f
    print(f)
    f='Changing to global variable'

someFunction()
globalFunction()
print(f)
d=11
print(d)
del d #delete variable
#print(d)