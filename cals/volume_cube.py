import math
import sys
sys.path.insert(1, '../')
import bot

def calculate():
    l = input('Enter Length: ')
    w = input('Enter Width: ')
    h = input('Enter Height: ')
    
    vol_cube = l * w * h
    
    return vol_cube