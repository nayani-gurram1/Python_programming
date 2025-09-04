def note(n):
    tm=0
    tm+=n//2000
    n=n%2000
    tm+=n//500
    n=n%500
    tm+=n//200
    n=n%200
    tm+=n//100
    n=n%100
    tm+=n//50
    n=n%50
    tm+=n//20
    n=n%20
    tm+=n//10
    n=n%10
    tm+=n//5
    n=n%5
    tm+=n//2
    n=n%2
    tm+=n//1
    n=n%1
    print("Total number of notes:",tm)
x=int(input("Enter the amount:"))
note(x)