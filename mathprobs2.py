import math

def squareFeet():
    length = int(input("What is the length of the house? "))
    width = int(input("What is the width of the house? "))
    return length * width 

def circum():
    diam = int(input("What is the diameter? "))
    return diam * math.pi