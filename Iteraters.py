# Python For & While Loops: Enumerate, Break, Continue Statement

def main():
    x=0
    Months=["Jan","Feb","Mar","Apr","May","Jun","Jul"]
    print("Months in a Year : ")
    for m in Months:
        print(m)
    while(x<4):
        print(x)
        x+= 1
if __name__ == '__main__':
    main()

for y in range(2,8):
    #if(y==5):break
    if(y%2==0):continue
    print("For Loop :",y)

# Enumerate - is used for the numbering or indexing the members in the list.
Months = ["Jan","Feb","Mar","April","May","June"]
for i,m in enumerate(Months):
    print(i,m)

for i in '123':
    print("Hello Number",i)