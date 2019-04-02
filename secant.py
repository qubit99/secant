# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 01:43:53 2019

@author: ARCHIT
"""
from math import *

tolerance = 10**(-6)

def f(x):
    f = x*x + sin(x) -5 #enter your function here
    return f

print("enter two guesses which should lie close to the actual root but need not bracket the solution.")

x0 = int(input("enter first guess "))
x1 = int(input("enter second guess "))
dx = abs(x1-x0)
while dx > tolerance:
    temp = x1
    x1 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
    x0 = temp
    dx = abs(x1 - x0)

print("The Root is",x0)

