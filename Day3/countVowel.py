def CountVowelConsonent():
    string=str(input("Enter string:"))
    vowel_count=0
    consonent_count=0
    for char in string:
        if char in ('a','e','i','o','u'):
            vowel_count=vowel_count+1
        else:
            consonent_count=consonent_count+1
    print("Total number of vowels are:",vowel_count)
    print("Total number of consonents are:",consonent_count)
CountVowelConsonent()
