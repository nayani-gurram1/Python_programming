def secondLarge():
    num=[10, 20, 4, 45, 99]
    largest=second_largest=float('-inf')
    for n in num:
        if n>largest:
            second_largest=largest
            largest=n
        elif n>second_largest and n!=largest:
            second_largest=n
    if second_largest==float('-inf'):
        print("No second largest element")
    else:
        print("Second largest element is:", second_largest)
secondLarge()