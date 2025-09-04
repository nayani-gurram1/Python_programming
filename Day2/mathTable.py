def mathTab():
    n=int(input("Enter a number for table:"))
    for i in range(1,11):
        res=n*i
        print(n,'*',i,'=',res)
mathTab()