num=[1,2,3,4,5,6,7]
i=0
even_count=0
odd_count=0
while i<len(num):
    if num[i]%2==0:
        even_count=even_count+1
    else:
        odd_count=odd_count+1
    i=i+1
print("Total even number:",even_count)
print("Total odd numbers",odd_count)