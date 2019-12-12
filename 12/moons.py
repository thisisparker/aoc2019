import math

class Moon:
    def __init__(self, xpos, ypos, zpos):
        self.xpos = xpos
        self.ypos = ypos
        self.zpos = zpos

        self.xvel = 0
        self.yvel = 0
        self.zvel = 0

    def calc(self, pos1, pos2, vel1):
        if pos1 > pos2:
            return vel1 - 1
        elif pos1 < pos2:
            return vel1 + 1
        elif pos1 == pos2:
            return vel1

    def gravity(self, other_moon):
        self.xvel = self.calc(self.xpos, other_moon.xpos, self.xvel)
        self.yvel = self.calc(self.ypos, other_moon.ypos, self.yvel)
        self.zvel = self.calc(self.zpos, other_moon.zpos, self.zvel)

    def move(self):
        self.xpos += self.xvel
        self.ypos += self.yvel
        self.zpos += self.zvel

    @property
    def potential(self):
        return abs(self.xpos) + abs(self.ypos) + abs(self.zpos)

    @property
    def kinetic(self):
        return abs(self.xvel) + abs(self.yvel) + abs(self.zvel)

    @property
    def total_energy(self):
        return self.potential * self.kinetic

i = """<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>"""

i = """<x=-19, y=-4, z=2>
<x=-9, y=8, z=-16>
<x=-4, y=5, z=-11>
<x=1, y=9, z=-13>"""

moons = []
states = set()
index = 1

for l in i.split('\n'):
    m = l.strip('<>').split(',')
    x = int(m[0][m[0].index('=')+1:])
    y = int(m[1][m[1].index('=')+1:])
    z = int(m[2][m[2].index('=')+1:])

    moons.append(Moon(x, y, z))

xcycle = False
ycycle = False
zcycle = False

xseen = set()
yseen = set()
zseen = set()


for _ in range(1000000):
    xstate = ()
    ystate = ()
    zstate = ()

    if xcycle and ycycle and zcycle:
        print(xcycle, ycycle, zcycle)
        break

    for moon in moons:
        others = [m for m in moons if m != moon]
        for o in others:
            moon.gravity(o)

    for moon in moons:
        moon.move()

        xstate = (*xstate, moon.xpos, moon.xvel)
        ystate = (*ystate, moon.ypos, moon.yvel)
        zstate = (*zstate, moon.zpos, moon.zvel)

    if not xcycle:
        if xstate in xseen:
            xcycle = _
        else:
            xseen.add(xstate)
    if not ycycle:
        if ystate in yseen:
            ycycle = _
        else:
            yseen.add(ystate)
    if not zcycle:
        if zstate in zseen:
            zcycle = _
        else:
            zseen.add(zstate)

    if index == 1000:
        energy = sum(moon.total_energy for moon in moons)

    if index % 100 == 0:
        print('step', index)

    index += 1

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

print('total energy at step 1000 is', energy)

print('x cycle:', xcycle)
print('y cycle:', ycycle)
print('z cycle:', zcycle)

print('exact duplicate in just', lcm(lcm(xcycle, ycycle), zcycle), 'steps!')
