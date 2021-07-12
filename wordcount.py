import operator

text_orig = '''enter text here'''

remove = [',','.','?','!','"','(',')','-']
for thing in remove:
    text_orig = text_orig.replace(thing,'')

word_list = text_orig.lower().split()
word_count = {}

for word in word_list:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_count = sorted(word_count.items(), key = operator.itemgetter(1), reverse = True)

print(f'There are {len(sorted_count)} unique words in the song!')

for word in sorted_count:
    print(f'{word[0].capitalize()} - {word[1]}')