def highFreq():
    num=input("Enter a string:")
    max_count=0
    max_char=""
    for ch in num:
        count=0
        for c in num:
            if c==ch:
                count+=1
        if count>max_count:
            max_count=count
            max_char=ch
    print("Highest frequency character:",max_char)
    print("Frequency:",max_count)
highFreq()
