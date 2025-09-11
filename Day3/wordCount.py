def wordCount():
    string=str(input("Enter string:"))
    count=0
    word=False
    for char in string:
        if char!= " " and not word:
            count+=1
            word=True
        elif char==" ":
            word=False
    print("Total number of words:", count)
wordCount()
