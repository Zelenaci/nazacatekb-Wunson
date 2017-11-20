# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 17:03:29 2017

@author: Ondra
"""

print("Fiboncciho sekvence")
p = int(input("kolik členů?:"))
print()
m = 0
n = 1
print(m)
while p > 1:
    print(n)
    n += m
    m = n-m
    p -= 1
print()