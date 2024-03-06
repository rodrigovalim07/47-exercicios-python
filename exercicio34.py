inicial = int(input('qual hora inicial? '))
final = int(input('qual hora final? '))
while ((inicial < 0) or (inicial > final) or (final < 0) or (inicial > 23) or (final > 24)):
    inicial = int(input('qual hora inicial? '))
    final = int(input('qual hora final? '))
for h in range (inicial, final, 1):
    for m in range (0, 60, 1):
        for s in range (0, 60, 1):
            print(h,':', m,':', s, 'hrs')