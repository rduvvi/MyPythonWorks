def fun1():
    print("I am learner here")
    print("Indention")

fun1()

def sqare(x):
    return x*x

print(sqare(4))
print(sqare)

def multiply(x,y=0):
    return x*y
print(multiply(4,5))

def fun2(*args):
    print(args)
    for x in args:
        print(x)
fun2(1,2,3,4,5)