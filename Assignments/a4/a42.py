#!/usr/bin/env python3
'''Assignment 4 Part 2'''
print(__doc__)

from operator import index
from typing import IO
import random

class ArtConfig:
    '''ArtConfig class'''
    def __init__(self, shape=None, x=None, y=None, radius=None, rx=None, ry=None, width=None, height=None, red=None, green=None, blue=None, op=None):
        
        # in order for easy use, if nothing is passed for this object declaration it will generate all the necessary attributes for a shape
        
        # random shape number generator
        if shape is None:
            randGen: GenRandom = GenRandom(0,2)
            self.shape: int = randGen.random
            
        # random x coordinate generator
        if x is None:
            randGen: GenRandom = GenRandom(0,1350)    
            self.x: int = randGen.random
        
        # random y coordinate generator
        if y is None:
            randGen: GenRandom = GenRandom(0,700)    
            self.y: int = randGen.random
            
        # random radius generator  
        if radius is None:
            randGen: GenRandom = GenRandom(0,100)
            self.radius: int = randGen.random
        
        # random rx generator  
        if rx is None:
            randGen: GenRandom = GenRandom(10,30)
            self.rx: int = randGen.random
          
        # random ry generator  
        if ry is None:
            randGen: GenRandom = GenRandom(10,30)
            self.ry: int = randGen.random
          
        # random width generator  
        if width is None:
            randGen: GenRandom = GenRandom(10,100)
            self.width: int = randGen.random
        # random height generator
        if height is None:
            randGen: GenRandom = GenRandom(10,100)
            self.height: int = randGen.random
            
        # random red color generator   
        if red is None:
            randGen: GenRandom = GenRandom(0,255)
            self.red: int = randGen.random
            
        # random green color generator 
        if green is None:
            randGen: GenRandom = GenRandom(0,255)
            self.green: int = randGen.random
            
        #random blue color generator 
        if blue is None:
            randGen: GenRandom = GenRandom(0,255)
            self.blue: int = randGen.random
            
        #random opacity generator
        if op is None: 
            self.op: float = random.random()
            
            
class GenRandom:
    '''GenRandom class'''
    def __init__(self, x: int, y: int):
        
        # generate random number between x and y values passed in
        self.x: int = x
        self.y: int = y
        self.random: int = random.randint(x,y)
        
       

def printRandomTable(numShapes: int):
    '''printRandomTable method'''
    
    # print columns for table
    print("{:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("CNT", "SHP", "X", "Y", "RAD", "RX", "RY", "WID", "HGT", "RED", "GRN", "BLU", "OP"))
    
    list_random_attributes = [] # create list for all random attributes
    
    # loop through numShapes times to create number of random attribute values
    for i in range(0, numShapes):
        
        GenRandomObject = ArtConfig() # create object for GenRandom class each time in loop for different values each time
        
        list_row = [] # create list to hold the row values for each shape
        
        # append each attribute value to list_row
        list_row.append(i)
        list_row.append(GenRandomObject.shape)
        list_row.append(GenRandomObject.x)
        list_row.append(GenRandomObject.y)
        list_row.append(GenRandomObject.radius)
        list_row.append(GenRandomObject.rx)
        list_row.append(GenRandomObject.ry)
        list_row.append(GenRandomObject.width)
        list_row.append(GenRandomObject.height)
        list_row.append(GenRandomObject.red)
        list_row.append(GenRandomObject.green)
        list_row.append(GenRandomObject.blue)
        list_row.append(round(GenRandomObject.op,1))
        
        list_random_attributes.append(list_row) # append row to overall list of random attributes
    
    # print rest of table of random attributes values 
    for random_attribute in list_random_attributes:
        print("{:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format(*random_attribute))
    

def main():
    '''main method'''
     
    num_shapes = 10 # specify number of shapes to generate values in the table
    
    printRandomTable(num_shapes) # print table with valuues specified in ArtConfig class
        
main()