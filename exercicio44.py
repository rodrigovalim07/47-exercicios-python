# DICIONARIOS
games = {'pes':'play 5', 'need for speed':'play 2', 'mortal kombat':'nintendo'}
print(games['pes'])
print(games.values())
print(games.keys())
print(games.items())
# ou para ficar mais bonito
for i in games.values():
    print(i)
for x in games.keys():
    print(x)