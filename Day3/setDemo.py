def set1():
    my_set=set()
    n=int(input("no.of elements:"))
    for i in range(n):
        ele=input(f"Enter element {i+1}:")
        my_set.add(ele)
        print("Set now:",my_set)
set1()
