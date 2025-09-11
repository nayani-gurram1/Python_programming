def dup():
    num=[1, 2, 3, 1, 1, 2, 3, 4, 2, 3, 4, 1]
    unique=[]
    for i in num:
        if i not in unique:
            unique.append(i)
    print("Without duplicates:",unique)
dup()
