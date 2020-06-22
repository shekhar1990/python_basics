# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 23:22:48 2020

@author: Shekhar.Maurya

Code Challenge
  Name: 
    Target Heart Rate Calculator
  Filename: 
    heartrate_cal.py
  Problem Statement:
    Calculate the Maximum Heart Rate and Target Heart Rate Range 
    ( Lower and Higher value ) of a person of a specific age.
    Lets Assume your age is 21 years
  Hint: 
    Subtract your age from 220 to get your Maximum Heart Rate
    Lower end of your Target Heart Rate is 70% of Maximum Heart Rate
    Higher end of your Target Heart Rate is 85% of Maximum Heart Rate
    Heart Rate = Beats per minute 
"""

Age = 21
Max_Heart_rate = 220 - Age
Lower_range = round(Max_Heart_rate *0.7)
Upper_range = round(Max_Heart_rate *0.85)
print("Maximum Heart Rate :",Max_Heart_rate)
print("Target Heart Rate Range :",Lower_range,"-",Upper_range)
