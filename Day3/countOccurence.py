def countOccurrence():
    string=str(input("Enter string:"))
    char=input("Enter character:")
    count = 0
    for c in string:
        if c == char:
            count += 1
    print(f"Character {char} occurs {count} times in the string.")
countOccurrence()