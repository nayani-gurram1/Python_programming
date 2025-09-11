def allOccurrence():
    string=str(input('Enter string:'))
    char=input("Enter character to search:")
    print(f"Occurrences of '{char}' in the string:")
    found=False
    for i in range(len(string)):
        if string[i]==char:
            print(f"Character found at position {i}")
            found=True
    if not found:
        print("Character not found in string")
allOccurrence()
