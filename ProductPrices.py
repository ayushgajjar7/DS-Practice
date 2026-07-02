# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:51:43 2026

@author: ayush
"""

# Sorted product prices
# Linear Search,
price = [50000, 71000, 17000, 20000, 90000, 10000]

target = 50000

for price in price:
    if price >= target:
        print("First price >= 50000 is:", price)
        break
    
# Out Put
#First price >= 50000 is: 50000