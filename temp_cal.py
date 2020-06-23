# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:49:22 2020

@author: Shekhar.Maurya

Code Challenge
  Name: 
    Temperature Calculator
  Filename: 
    temp_cal.py
  Problem Statement:
    Assume today's temperature in Jaipur is 29 degree Centigrade. 
    Calculate the temperate in Degree Fahrenheit and print it.
    Calculate the temperature in Degree Kelvin and print it.
  Hint: 
    Multiply by 9/5 and add 32  to get in Fahrenheit
    Add 273 approximately to get in Kelvin
"""
temp = 29.0
Fahren = temp*(9/5)+32
Kelvin = temp + 273
print("temperate in Degree Fahrenheit :",Fahren)
print("temperate in Degree Kelvin :",Kelvin)
