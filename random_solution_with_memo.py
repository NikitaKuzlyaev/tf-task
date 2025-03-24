import sys
import random

field = [['#'] * 12 for i in range(12)]
for i in range(1, 11):
    for j in range(1, 11):
        field[i][j] = '?'

x, y = 1, 1
vectors = {
    'right': lambda x, y: [x, y + 1],
    'up': lambda x, y: [x - 1, y],
    'left': lambda x, y: [x, y - 1],
    'down': lambda x, y: [x + 1, y],
}

field[1][1] = '.'

while True:

    while True:
        query = random.choice(['down', 'up', 'left', 'right'])
        nx, ny = vectors[query](x, y)

        if field[nx][ny] != '#':
            break

    print(query)
    sys.stdout.flush()

    response = str(input())

    if response == 'end':
        break
    elif response == 'auch':
        field[nx][ny] = '#'
    elif response == 'ok':
        x, y = nx, ny
