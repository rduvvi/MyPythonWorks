# in Python strings are immutable

var1 = "Guru99!"
var2 = "Software Training"
print("String values : "+var1 +"==="+ var2)
print("var1[0]:",var1[0])
print("var2[1:5]",var2[1:5])
x="Guru"
print(x[1:3]) # Range slice-it gives the characters from the given range
print("u" in x) # Membership-returns true if a letter exist in the given string
print("l" not in x) # Membership-returns true if a letter exist is not in the given string

print(r'\n') # Raw string suppresses actual meaning of escape characters.

name='guru'
number=99
print('%s %r' %(name,number))

print(2*name) # It prints the character twice.

w="Hello World"
print(w[:6]+"Roshan")

oldstring = "I like myself"
newstring=oldstring.replace("like","love")
print(newstring+"==Upper : "+newstring.upper()+"==Lower : "+newstring.lower())

print(":".join("Python")) # join function
print("".join(reversed(newstring))) # reverse

word="guru99 career guru99"
print(word.split(' ')) # split with space and 'r'
x2=word.replace("career","hello")
print(x2)

a = {'x1':100, 'y1':200}
print(list(a.items()))