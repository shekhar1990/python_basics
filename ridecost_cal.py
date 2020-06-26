# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 15:04:39 2020

@author: Shekhar.Maurya
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
 """
travel = 80
diesel = 80
average = 18
fuel = travel/average
print("cost of driving per day to office :", round(fuel*diesel))