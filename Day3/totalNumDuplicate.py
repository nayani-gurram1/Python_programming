def countDup():
    num=[1, 2, 3, 1, 1, 2, 3, 4, 2, 3, 4, 1]
    frq={}
    for i in num:
        if i in frq:
            frq[i] += 1
        else:
            frq[i] = 1
    dup_count=0
    for value in frq.values():
        if value>1:
            dup_count+=1
    print("Total number of duplicate elements:", dup_count)
countDup()