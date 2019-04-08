def flip_lydias(i):
    _ = int(input())
    path = str(input())
    flipped_path = []
    for move in path:
        if move == 'S':
            flipped_path.append('E')
        else:
            flipped_path.append('S')

    return 'Case #{}: {}'.format(i, ''.join(flipped_path))


t = int(input())
results = []
for i in range(1, t + 1):
    results.append(flip_lydias(i))


for result in results:
    print(result)
