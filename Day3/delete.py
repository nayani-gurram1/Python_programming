def dele():
    num=[1,2,3,4,5,6,7]
    print(num)
    i=int(input("Enter the position to delete element:;"))
    if 0 <= i < len(num):
        num.pop(i)
        print("Updated list:", num)
    else:
        print("Invalid position!")
dele()