def lowfreq():
    num=input("Enter a string: ")
    freq = {}
    for ch in num:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
    min_char=min(freq,key=freq.get)
    print("Lowest frequency character:",min_char)
    print("Frequency:",freq[min_char])
