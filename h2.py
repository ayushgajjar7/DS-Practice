# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 23:18:35 2026

@author: ayush
"""

size = 5
q = [None] * size
f = -1
r = -1

def enq(vehicle):
    global f, r

    if (r + 1) % size == f:
        print("full")
        return

    if f == -1:
        f = r = 0
    else:
        r = (r + 1) % size

    q[r] = vehicle
    print(vehicle, "Entered.")

def deq():
    global f, r

    if f == -1:
        print("tol Empty")
        return

    print(q[f], "left.")

    if f == r:
        f = r = -1
    else:
        f = (f + 1) % size

def dis():
    if f == -1:
        print("Empty")
        return

    print("Vehicles:",end='')
    i = f
    while True:
        print(q[i], end=" ")
        if i == r:
            break
        i = (i + 1) % size
    print()



enq("Car")
enq("Bus")
enq("Truck")
dis()
deq()
dis()