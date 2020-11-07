#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Length conversions
def toMeters(feet):
    return feet / 3.2808399

def toFeet(meters):
    return meters * 3.2808399

#Mass conversions
def toKilograms(pounds):
    return pounds / 2.20462262

def toPounds(kilograms):
    return kilograms * 2.20462262

#Temperature conversions
def toCelsius(kelvin):
    return kelvin - 273.15

def toKelvin(celsius):
    return celsius + 273.15

#Time conversions
def toSeconds(hours):
    return hours * 3600

def toHours(seconds):
    return hours / 3600

