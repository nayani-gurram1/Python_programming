def threeHigh(a,b,c):
    if(a>b):
        if(a>c):
            print("a is greater")
        else:
            print("c is greater")
    else:
        if(b>c):
            print("b is graeter")
        else:
            print("c is greater")
print("Enter three numbers:")
x=int(input("Number1:"))
y=int(input("Number2:"))
z=int(input("Number3:"))
threeHigh(x,y,z)