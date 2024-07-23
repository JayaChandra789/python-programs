a = input("Enter string: ")
vowels = 0
cons = 0
vowel_list = []
cons_list = []
for i in range(len(a)):
    if a[i] != ' ':
        if a[i] in 'aeiouAEIOU':
            vowels += 1
            vowel_list.append(a[i])
        else:
            cons += 1
            cons_list.append(a[i])

print("Vowels count= ",vowels)
print("Vowels present= ", ', '.join(vowel_list))
print("Consonants count= ",cons)
print("Consonants present= ", ', '.join(cons_list))


      
