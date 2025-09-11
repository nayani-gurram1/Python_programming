def CountAll():
    string=str(input("Enter string:"))
    alpha_count=0
    digit_count=0
    specialChar_count=0
    for char in string:
        if char.isalpha():
            alpha_count=alpha_count+1
        elif char.isdigit():
            digit_count=digit_count+1
        else:
            specialChar_count=specialChar_count+1
    print("Total number of alphabets:",alpha_count)
    print("Total number of Digits:",digit_count)
    print("Total number of special characters:",specialChar_count)
CountAll()