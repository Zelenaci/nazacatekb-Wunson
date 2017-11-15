# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:31:36 2017

@author: Ondra
"""


def pyramida1(r):
    print()
    h = r
    while h > 0:
        print(h*"*")
        h -= 1

def pyramida2(r):
    m = r
    h = 1
    print()
    while m > 0:
        print(m*" " + h*"*")
        h += 2
        m -= 1

def pyramida3(r):
    print()
    h = 1
    polovina = r//1
    while r > polovina:
        print(h*"*")
        h += 1
        r -= 1
    while r >= 0:
        print(h*"*")
        h -= 1
        r -= 1
    

r = int(input(">>"))        
pyramida1(r)
pyramida2(r)
pyramida3(r)