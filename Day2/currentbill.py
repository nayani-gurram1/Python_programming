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
tu=tu-50
cbill=(50*3.80)+tu*4.20+(tu-100*5.10)+(tu-150*6.30)+(tu-200*7.50)
print("Current bill:",cbill)