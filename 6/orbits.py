with open('orbits.txt') as f:
    orbits = f.readlines()
    orbits = [o.strip() for o in orbits]

directs = {}

for o in orbits:
    r = o.split(')')
    directs[r[1]] = r[0]

directs['COM'] = []

indirects = {}

for d in directs.keys():
    center = directs[d]
    indirects[d] = []
    while center:
        indirects[d].append(center)
        center = directs[center]

print('there are', len(indirects), 'planets')
print('for a total of', sum(len(lst) for lst in indirects.values()))

hops = 0

for planet in indirects['YOU']:
    if planet in indirects['SAN']:
        hops += indirects['SAN'].index(planet)
        break
    else:
        hops += 1

print('to get to santa you have to hop', hops, 'orbits')

