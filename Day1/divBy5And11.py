def num(n):
    if(n%5==0 and n%11==0):
        print("Number is divisible by 5 & 11")
    else:
        print("It is not divisible by 5 & 11")
x=int(input("Enter number:"))
num(x)