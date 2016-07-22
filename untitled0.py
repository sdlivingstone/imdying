# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 09:38:13 2016

@author: student
"""

def mixedfun(num):
    if num > 100:
        if num%2==0:
            print("big/even")
        else:
            print("Odd/Big")
    else: 
        if num%2 ==0:
            print("Small/Even")
        else:
            print("Small/Odd")
num=int(input("Write a Number")

mixedfun(num)