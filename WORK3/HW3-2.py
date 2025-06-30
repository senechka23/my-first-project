word = input ("enter a word in small latin letters")

vowels = 0
consonants = 0

for letter in word:
     if 'a' <= letter <= 'z':
          if letter in "aeiou":
               vowels += 1
          else:
               consonants += 1
     else:
          print (False)

print ("number of vowels letters:", vowels)
print("number of consonants letters:", consonants)