# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:55:15 2026

@author: ayush
"""

size=8
p_list=[]


def push(product):
    if len(p_list)==size:
        print("Belt is Full")
    else:
        p_list.append(product)
        print(f"{product} is added..")
        
def peek():
    if p_list:
        print(f"top product {p_list[0]}")
    else:
        print("Belt is empty")
        
def update(product):
    if p_list:
        p_list[0]=product
        print("Top product updated")
        print(p_list)
    else:
        print("Belt is empty")
    
def is_full():
    if len(p_list)==size:
        print("Belt is Full")
    else:
        print("space is available")
push('laptop')
push("phone")
peek()
update('table')
is_full()