import random
sentence = input('Sentence: ')
words = sentence.split()

for i in range(0, len(words)):
    t = random.randint(0, len(words) - 1)   # Needs fixing
    print(words[t])
