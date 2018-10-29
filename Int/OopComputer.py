class Computer:
 print("Hello")
 def __init__(self,cpu,ram):
         self.you = cpu
         self.age=ram
 def confin(self):
     print("System Configuration values",self.age,self.you)

com1=Computer('CoreI7',26)
com1.confin()