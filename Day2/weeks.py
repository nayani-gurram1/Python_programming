def week(n):
    if(n==1):
        print("Sunday")
    elif n==2:
        print("Monday")
    elif n==3:
        print("Tuesday")
    elif n==4:
        print("Wednesday")
    elif n==5:
        print("Thursday")
    elif n==6:
        print("Friday")
    elif n==7:
        print("Saturday")
    else:
        print("Enter 1 to 7 only")
x=int(input("Enter 1 to 7 to any week:"))
week(x)