cno=int(input("Consumer number:"))
cn=input("Consumer name:")
pmr=int(input("present month reading:"))
lmr=int(input("last month reading:"))
tu=pmr-lmr
print("Consumer no:",cno)
print("Consumer name:",cn)
print("present nomth readind:",pmr)
print("last month reading:",lmr)
print("Total units:",tu)
cbill=tu*3.80
print("Current bill:",cbill)