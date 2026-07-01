# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:00:30 2026

@author: ayush
"""

b = []
f = []
cur = "Home"

def visit(place):
    global car
    b.append(car)
    car = place
    f.clear()
    print("cur Location:", car)

def back():
    global car
    if not b:
        print("No Previous Location")
    else:
        f.append(car)
        car = b.pop()
        print("Car Location:", car)

def forward():
    global car
    if not f:
        print("No Forward Location")
    else:
        b.append(cur)
        car = f.pop()
        print("Carr Location:", car)

visit("Mall")
visit("Hospital")
visit("Airport")

back()
back()
forward()