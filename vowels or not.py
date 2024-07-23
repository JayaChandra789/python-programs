

def vowels():
 vowels=(input("Enter name"))
 list1=(a,e,i,o,u,A,E,I,O,U)
if vowels==list1:
 vowels=[]
 print("vowels are",vowels,vowels.count(vowels))
else:
 list2=(b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z)
 consonants=[]
 print("consonants are",consonants,consonants.count(consonants))
 
'''
def count_vowels_consonants():
    name = input("Enter a name: ")
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    vowel_count = 0
    consonant_count = 0
    
    for char in name:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    print("Vowels:", vowel_count)
    print("Consonants:", consonant_count)

count_vowels_consonants()
'''
