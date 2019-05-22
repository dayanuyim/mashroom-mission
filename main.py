#!/usr/bin/env ptyhon3

from collections import namedtuple

Mashroom = namedtuple('Mashoom', ['name', 'str', 'int', 'speed', 'special'])
mashrooms = [
    Mashroom('normal', 150, 150, 150, ('luck', 'stone', 'weapon')),
    Mashroom('white', 160, 100, 100, ('naive')),
    Mashroom('devil', 85, 90, 160, ('stone', 'horn')),
]

Act = namedtuple('Act', ['number', 'attr', 'threshold', 'cond', 'special'])
mission = [
    Act(1, 'str', 15, None, None),
    Act(1, 'str', 60, None, (1, 'has', 'luck', 50)),
]


print(mashrooms)
print(mission)