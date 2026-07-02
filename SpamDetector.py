# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 21:49:02 2026

@author: ayush
"""

# Spam Detector (Linear Search)

# List of blacklisted sender IDs
blacklist = ["ayush123", "harpal856", "aafridi039", "rahul111"]

# Sender ID to search
a = input("Enter sender ID : ")

# Check each ID one by one
for i in blacklist:
    if i == a:
        print("Spam sender is found")
        break
else:
    print("Sender is safe")