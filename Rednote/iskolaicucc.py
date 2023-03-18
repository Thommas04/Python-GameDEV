
'''
olvass be egy mondatot,
írd ki hány szóból áll a mondat
majd írd ki hány c betű van benne,
hány betűből áll
'''

sentence = str(input("Írj be egy mondatot: "))
letters = 0
c = 0

splitted = sentence.split(" ")

for i in sentence:
    if i not in [' ','.','?','!','-',',']:
        letters += 1
    if i == 'c':
        c += 1

print(f'{len(splitted)} szóból áll a mondat')
print(f'{c} darab c betű van a mondatban')
print(f'{letters} darab betű van a mondatban')