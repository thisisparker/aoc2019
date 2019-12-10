from math import atan2, pi

with open('asteroids.txt') as f:
    a = [l.strip() for l in f.readlines()]

asteroids = []

for y in range(len(a)):
    for x in range(len(a[y])):
        if a[y][x] == '#':
            asteroids.append((x,y))

visible = {}

for loc in asteroids:
    others = [ast for ast in asteroids if ast != loc]

    visible[loc] = set()
    
    for ast in others:
        visible[loc].add(atan2((loc[1]-ast[1]), (ast[0]-loc[0])))

spot = max(visible, key=lambda x: len(visible[x]))

print("the best spot for an asteroid observatory is", spot, "with",  len(visible[spot]), "visible asteroids")

rads = [rad for rad in visible[spot]]

q1 = list(reversed(sorted([a for a in rads if a > 0 and a <= pi/2])))
q2 = list(reversed(sorted([a for a in rads if a > pi/2 and a <= pi])))
q3 = list(reversed(sorted([a for a in rads if a > -pi and a <= -pi/2])))
q4 = list(reversed(sorted([a for a in rads if a > -pi/2 and a <= 0])))

quads = q1 + q4 + q3 + q2

for ast in asteroids:
    if atan2((spot[1]-ast[1]), (ast[0]-spot[0])) == quads[199]:
        print("200th vaporized asteroid is", ast)
