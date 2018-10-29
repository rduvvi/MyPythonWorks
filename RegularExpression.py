# Python Regex: re.match(), re.search(), re.findall() with Example
import re
x="welcom roshan to regular experssion"
r1=re.findall(r"^\w+",x)
print(r1)

#Example of \s expression in re.split function
print((re.split(r"\s","we are splitting the words")))
print((re.split(r"s","splitting the words")))
#Using re.match()
list=["muru99 get","guru99 give","guru99 selenium"]
for elemnts in list:
    z=re.match("(g\w+)\W(g\w+)",elemnts)
    if z:
        print((z.group()))

#re.search()
pattern=["roshan is an intelligent","roshan"]
text="roshan is an intelligent boy"
for x in pattern:
    print("Looking for %s in %s -->" %(x,text),end=' ')
    if re.search(x, text):
        print("Match found")
    else:
        print("no match")

#re.findall()
abc='guru99@gmail.com,mymail@hotmail.com,career@yahoo.com'
emails=re.findall(r'[\w\.-]+@[\w\.-]+',abc)
for email in emails:
    print(email)

# Python Flags - Python flags like re.U (Unicode), re.L (Follow locale), re.X (Allow Comment), etc.
xx="""guru99
careerguru99
roshan115"""
k1=re.findall(r"^\w",xx)
k2=re.findall(r"^\w",xx,re.MULTILINE)
print(k1)
print(k2)