def prime():
    i=1
    n=int(input("Enter a number:"))
    while i<n:
        i=i+1
        if(n%i==0):
            print("not a number")
            return
        else:
            i=i+1
    print("prime number")
prime()
        
