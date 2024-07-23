def count_vowels_consonants():
    name = input("Enter a name: ")
    vowels = "aeiouAEIOU"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in name:
        if char in vowels:
            vowel_count += 1
    
    print("Vowels:")
    for vowel in vowels:
        count = name.lower().count(vowel.lower())
        if count > 0:
            print(f"{vowel}: {count}")

    consonant_count = len(name) - vowel_count
    print("Consonants:", consonant_count)

count_vowels_consonants()
