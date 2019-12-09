with open('input.txt') as f:
    raw = f.read().strip()

layers = []

for lcount in range(100):
    layers.append([int(raw[150 * lcount + digit]) for digit in range(150)])

l = min(layers, key=lambda x: x.count(0))

print(l)


print(len(l))

print(l.count(1) * l.count(2))

visible = []

for index in range(150):
    for layer in layers:
        if layer[index] != 2:
            visible.append(layer[index])
            break

print(visible)

for row in range(6):
    print(''.join(' ' if i == 0 else '#' for i in visible[25*row:25*(row+1)]))
