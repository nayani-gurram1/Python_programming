def leap(n):
    if((n%400==0 and n%100!=0) or n%4==0):
        print("It is a leap year")
    else:
        print("It is not a leap year")
x=int(input("Enter a year:"))
leap(x)