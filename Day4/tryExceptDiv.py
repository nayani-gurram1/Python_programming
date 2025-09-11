num=int(input("Enter numerator:"))
den=int(input("Enter denominator:"))
try:
    result=num/den
    print("Result:",result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed")