def palindrome():
    n=int(input("Enter the number:"))
    sum=0
    while n>0:
        res=n%10
        sum=sum*10+res
        n=n//10
    print(sum)
palindrome()