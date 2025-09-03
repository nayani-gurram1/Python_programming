PA=int(input("Enter the principle amount:"))
time=int(input("time taken:"))
r=int(input("rate of interest:"))
SI=PA*time*r/100
print("Simple interest:",SI)
total_amount=SI+PA
print("Total amount:",total_amount)