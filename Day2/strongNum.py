def fact():
    n=int(input("Enter the number:"))
    factorial=1
    while i<n:
        i=i+1
        factorial=factorial*i
def strongNum(number):
    num_str=str(number)
    sum=0
    for i in num_str:
        i=int(i)
        dig_fac=fact(i)
        sum+=dig_fac
    if sum==number:
        return True
    else:
        return False
x=int(input("Enter the number:"))
if (strongNum(x)):
    print("The strong number are:",x)
else:
    print("It is not a strong number")
    