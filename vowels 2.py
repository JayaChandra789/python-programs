def vowels_conut(name):
 vowels=("aeiouAEIOU")
 vowels=[]
 for char in name:
  if char in vowels:
   vowels_count+=1
   return vowels_count
name=input("Enter a string")
print("vowels in the name are",vowels)

'''
def count_vowels(name):
    vowels = "aeiouAEIOU"
    vowels_count = 0
    
    for char in name:
        if char in vowels:
            vowels_count += 1
    
    return vowels_count

name = input("Enter a string: ")
vowels_count = count_vowels(name)
print("Number of vowels in the name are:", vowels_count)




consonants=("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
 vowels=[]
 consonants=[]
for char in name:
    if vowels in name:
        vowel_count+=1
    print("vowels are",vowels)'''
 
