def sumDigit():
    n=int(input("Enter the number:"))
    sum=0
    while n>0:
        res=n%10
        sum=sum+res
        n=n//10
    print(sum)
sumDigit()