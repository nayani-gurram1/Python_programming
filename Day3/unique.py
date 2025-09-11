def uniq():
    num=[1,2,3,1,1,2,3,4,2,3,4,1]
    num.sort()
    print(num)
    frq={}
    for i in num:
        if i in frq:
            frq[i]=frq[i]+1
        else:
            frq[i]=1
    for key,value in frq.items():
        if value==1:
            print(key)
uniq()