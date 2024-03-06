x = 10
while(x <= 20):
    for j in range(10, 20, 2):
        print('{} + {} = {}'.format(x, j, x + j))
    x += 1