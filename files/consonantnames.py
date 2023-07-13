# take consonants from consonant1.txt to consonant2.txt

f=open('consonant1.txt', 'r')
f1=open("consonant2.txt", 'w')

vowels='aeiou'

for i in f:
    if i[0] not in vowels:
        f1.write(i)





