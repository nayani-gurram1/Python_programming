def CheckChar(n):
    if n.isalpha():
        print("It is an alphabet")
    elif (n.isdigit()):
        print("It is a digit")
    else:
        print("It is a special character")
x=input("Enter any charactter:")
CheckChar(x)