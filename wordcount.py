import operator

text_orig = '''Yuh, ooh, brr, brr
Gucci gang, ooh
(That's it right there, Gnealz)
Yuh, Lil Pump, yuh
Gucci gang, ooh
(Ooh, Bi-Bighead on the beat)
Yuh, brr
Gucci gang, Gucci gang, Gucci gang, Gucci gang (Gucci gang)
Gucci gang, Gucci gang, Gucci gang, Gucci gang (Gucci gang)
Spend three racks on a new chain (Yuh)
My bitch love do cocaine, ooh (Ooh)
I fuck a bitch, I forgot her name (Brr, yuh)
I can't buy a bitch no wedding ring (Ooh)
Rather go and buy Balmains (Brr)
Gucci gang, Gucci gang, Gucci gang (Gucci gang)
Gucci gang, Gucci gang, Gucci gang
Gucci gang, Gucci gang, Gucci gang, Gucci gang (Gucci gang)
Spend three racks on a new chain (Huh?)
My bitch love do cocaine, ooh (Brr)
I fuck a bitch, I forgot her name, yuh (Yuh, yuh)
I can't buy no bitch no wedding ring, ooh (Nope)
Rather go and buy Balmains, ayy (Brr)
Gucci gang, Gucci gang, Gucci gang (Gucci gang)
My lean cost more than your rent, ooh (It do)
Your momma still live in a tent, yuh (Brr)
Still slangin' dope in the 'jects, huh? (Yeah)
Me and my grandma take meds, ooh (Huh?)
None of this shit be new to me (Nope)
Fuckin' my teacher, call it tutory (Yuh)
Bought some red bottoms, cost hella G's (Huh?)
Fuck your airline, fuck your company (Fuck it!)
Bitch, your breath smell like some cigarettes (Cigarettes)
I'd rather fuck a bitch from the projects (Yuh)
They kicked me out the plane off a Percocet (Brr)
Now Lil Pump flyin' private jet (Yuh)
Everybody scream, "Fuck WestJet" (Fuck 'em)
Lil Pump still sell that meth (Yuh)
Hunnid on my wrist, sippin' on Tech (Brr)
Fuck a lil' bitch, make her pussy wet (What?)
Gucci gang, Gucci gang, Gucci gang
Gucci gang, Gucci gang, Gucci gang, Gucci gang (Gucci gang)
Spend three racks on a new chain (Huh?)
My bitch love do cocaine, ooh (Yuh)
I fuck a bitch, I forgot her name (Brr)
I can't buy a bitch no wedding ring (Huh?)
Rather go and buy Balmains (Yuh)
Gucci gang, Gucci gang, Gucci gang (Gucci gang)
Gucci gang, Gucci gang, Gucci gang, Gucci gang
Gucci gang, Gucci gang, Gucci gang (Gucci gang)
Spend three racks on a new chain (Huh?)
My bitch love do cocaine, ooh (Brr)
I fuck a bitch, I forgot her name, yuh (Yuh)
I can't buy no bitch no wedding ring, ooh (Nope)
Rather go and buy Balmains, ayy (Huh?)
Gucci gang, Gucci gang, Gucci gang (Gucci gang)'''

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