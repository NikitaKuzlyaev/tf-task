import sys
 
field = [['#'] * 12 for i in range(12)]
for i in range(1, 11):
    for j in range(1, 11):
        field[i][j] = '?'
 
flag = True
x, y = 1, 1
vectors = {'down': lambda x, y: [x + 1, y],
           'up': lambda x, y: [x - 1, y],
           'left': lambda x, y: [x, y - 1],
           'right': lambda x, y: [x, y + 1],
           }
 
reverse_names = {
    'down': 'up',
    'up': 'down',
    'left': 'right',
    'right': 'left',
}
 
stack = []
field[1][1] = '.'
 
while True:
    # тут делаю запрос
    q_dir = 'down'
 
    for direction_name, transform in vectors.items():
        nx, ny = transform(x, y)
 
        if field[nx][ny] == '?':
            q_dir = direction_name
            break
 
    else:
        if len(stack) > 0:
            px, py, dir_name = stack.pop()
            rev_name = reverse_names[dir_name]
            q_dir = rev_name
 
    print(q_dir)
    sys.stdout.flush()
    f = str(input())
 
    if f == 'end':
        break
 
    if f == 'ok':
        nx, ny = vectors[q_dir](x, y)
        if field[nx][ny] == '?':
            stack.append([x, y, q_dir])
        x, y = nx, ny
        field[x][y] = '.'
      
    elif f == 'auch':
        nx, ny = vectors[q_dir](x, y)
        field[nx][ny] = '#'
