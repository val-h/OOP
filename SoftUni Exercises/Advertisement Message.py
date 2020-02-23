import random
numRev = int(input('Number of reviews: '))

# Preset phrases
phrases = ('Excelent product.', 'Such a great product.', 'I always use that product.',
 'Best product of its category.', 'Exceptional product.', 'I can\'t live without this product.')
events = ('Now i feel good.', 'I have succeeded with this product.', 'Makes miracles. I am happy of the results!',
'I cannot belive but now i fell awesome.', 'Try it yourself, i am very satisfied.', 'I feel great!')
authors = ('Diana', 'Petya', 'Stella', 'Elena', 'Katya', 'Iva', 'Annie', 'Eva')
cities = ('Burgas', 'Sofia', 'Plovdiv', 'Varna', 'Ruse')

# Creates a sentence from random pieces of the lists above
def SentenceConstructor():
    phrase = random.choice(phrases)
    event = random.choice(events)
    author = random.choice(authors)
    city = random.choice(cities)
    return f'{phrase} {event} {author} - {city}'

for i in range(0, numRev):
    print(SentenceConstructor())
