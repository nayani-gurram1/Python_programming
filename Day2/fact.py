def fact():
    i=0
    n=int(input("Enter the number:"))
    factorial=1
    while i<n:
        i=i+1
        factorial=factorial*i
    print(factorial)
fact()
