#Python OOPs: Class, Object, Inheritance and Constructor with Example

class myClass():
    def fun1(self):
        print("My First Func in class")
    def fun2(self):
        print(3*5)
#Inheriatnce
class childClass(myClass):
    def fun1(self):
        myClass.fun1(self);
        print("Child Methond 1")
    def fun2(self):
        print("Child class")
class User:
    name = ""
    def __init__(self,name):
     self.name=name
    def sayHello(self):
      print("Welocome "+self.name+"...!")

u = User("Roshan")
u.sayHello();
def main():
    """
     c=myClass()
     c.fun1()
     c.fun2()
     """
    c2=childClass()
    c2.fun2();
    c2.fun1();


if __name__=="__main__":
    main()