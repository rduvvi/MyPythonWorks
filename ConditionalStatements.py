def main():
    x=4
    y=5
    if(x>y):
        print("x is > than y")
    else:
        print("x is < than y")

if __name__=="__main__":
    main()
def Confunc():
    x,y=8,8
    if(x<y):
        print("x < y")
    elif(x==y):
        print("x==y")
    else:
        print("x > y")
Confunc()

# execute conditional statement with minimal code

def minval():
    v=3
    m=6
    st="v is less than m" if(v<m) else "v is more than m"
    print(st)
minval()

# Switch statement - A switch statement is a multiway branch statement that compares the value of a variable to the values specified in case statements.

# Python language doesn’t have a switch statement.
# Python uses dictionary mapping to implement switch statement in Python
def SwitchExample(argument):
    switcher = {
               0: "THis is Zero case ",
               1: "This is One Case ",
               2: "This is Two case",
               }
    return switcher.get(argument,"nothing")

argument=1
print(SwitchExample(argument))

