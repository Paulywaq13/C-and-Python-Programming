#!/usr/bin/env python3
'''Assignment 4 Part 3'''
print(__doc__)

from typing import IO
import random

class Circle:
    '''Circle class'''
    def __init__(self, cir: tuple, col: tuple):
        
        # get the radius and center of the circle from tuple
        self.cx: int = cir[0]
        self.cy: int = cir[1]
        self.rad: int = cir[2]
        
        # get the color of the circle and opacity from tuple
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        
    
class Rectangle:
    '''Rectangle class'''
    def __init__(self, rec: tuple, col: tuple):
        
        # get the width and height of the rectangle from tuple
        self.x: int = rec[0]
        self.y: int = rec[1]
        self.rwidth: int = rec[2] 
        self.rheight: int = rec[3]
        
        # get the color of the rectangle and opacity from tuple
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        
        
class Ellipse:
    '''Ellipse class'''
    def __init__(self, ell: tuple, col: tuple):
        
        # get the width, height and centre of the ellipse from tuple
        self.cx: int = ell[0]
        self.cy: int = ell[1]
        self.rx: int = ell[2]
        self.ry: int = ell[3]
        
        # get the color of the ellipse and opacity from tuple
        self.red: int = col[0]
        self.green: int = col[1]
        self.blue: int = col[2]
        self.op: float = col[3]
        
        
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
 

class ProEpilogue:
    """ProEpilogue class"""
    
    def writeHTMLHeader(self, f: IO[str], winTitle: str) -> None:
        '''writeHeadHTML method'''
        writeHTMLline(f, 0, "<html>")
        writeHTMLline(f, 0, "<head>")
        writeHTMLline(f, 1, f"<title>{winTitle}</title>")
        writeHTMLline(f, 0, "</head>")
        writeHTMLline(f, 0, "<body>")
        
    def openSVGcanvas(self, f: IO[str], t: int, canvas: tuple) -> None:
        '''openSVGcanvas method'''
        ts: str = "   " * t
        writeHTMLcomment(f, t, "Define SVG drawing box")
        f.write(f'{ts}<svg width="{canvas[0]}" height="{canvas[1]}">\n')
    
    def closeSVGcanvas(self, f: IO[str], t: int) -> None:
        '''closeSVGcanvas method'''
        ts: str = "   " * t
        f.write(f'{ts}</svg>\n')
        f.write(f'</body>\n')
        f.write(f'</html>\n')       
    
        
def writeHTMLcomment(f: IO[str], t: int, com: str) -> None:
    '''writeHTMLcomment method'''
    ts: str = "   " * t
    f.write(f'{ts}<!--{com}-->\n')
        
def drawCircleLine(f: IO[str], t: int, c: Circle) -> None:
    '''drawCircle method'''
    ts: str = "   " * t
    line: str = f'<circle cx="{c.cx}" cy="{c.cy}" r="{c.rad}" fill="rgb({c.red}, {c.green}, {c.blue})" fill-opacity="{c.op}"></circle>'
    f.write(f"{ts}{line}\n")
    
def drawRectangleLine(f: IO[str], t: int, r: Rectangle) -> None:
    '''drawRectangle method'''
    ts: str = "   " * t
    line: str = f'<rect x="{r.x}" y="{r.y}" width="{r.rwidth}" height="{r.rheight}" fill="rgb({r.red}, {r.green}, {r.blue})" fill-opacity="{r.op}"></rect>'
    f.write(f"{ts}{line}\n")
    
def drawEllipseLine(f: IO[str], t: int, e: Ellipse) -> None:
    '''draEllipse method'''
    ts: str = "   " * t
    line: str = f'<ellipse cx="{e.cx}" cy="{e.cy}" rx="{e.rx}" ry="{e.ry}" fill="rgb({e.red}, {e.green}, {e.blue})" fill-opacity="{e.op}"></ellipse>'
    f.write(f"{ts}{line}\n")
        
def genArt(numShapes: int, f: IO[str], t: int) -> None:
   '''genART method'''
   
   # for amount of shapes assigned to numShapes, create random shapes of circle, ellipse and rectangles
   
   for i in range(0,numShapes):
       
        genRandomObject = ArtConfig() # create random attriburtes object
        
        # if 0 value generated in shape attribute, generate circle
        if genRandomObject.shape == 0:
            drawCircleLine(f, t, Circle((genRandomObject.x, genRandomObject.y, genRandomObject.radius), (genRandomObject.red, genRandomObject.green, genRandomObject.blue, genRandomObject.op)))
        
        # if 1 value generated in shape attribute, generate ellipse
        elif genRandomObject.shape == 1:
            drawRectangleLine(f, t, Rectangle((genRandomObject.x, genRandomObject.y, genRandomObject.width, genRandomObject.height), (genRandomObject.red, genRandomObject.green, genRandomObject.blue, genRandomObject.op)))
        
        # if 2, the only value remaining value generated in shape attribute, generate rectangle
        else:
            drawEllipseLine(f, t, Ellipse((genRandomObject.x, genRandomObject.y, genRandomObject.rx, genRandomObject.ry), (genRandomObject.red, genRandomObject.green, genRandomObject.blue, genRandomObject.op)))
   
   
def writeHTMLline(f: IO[str], t: int, line: str) -> None:
    '''writeLineHTML method'''
    ts = "   " * t
    f.write(f"{ts}{line}\n")


def writeHTMLfile(numShapes: int) -> None:
    '''writeHTMLfile method'''
    fnam: str = "a43.html" # filename
    winTitle = "My Art3" # art title
    
    f: IO[str] = open(fnam, "w") # open file for writing
    
    ProEpi = ProEpilogue() # create ProEpilogue object
    
    ProEpi.writeHTMLHeader(f, winTitle) # write header to file using writeHTMLHeader method in ProEpilogue class
    
    ProEpi.openSVGcanvas(f, 0, (10000,10000)) # open SVG canvas using openSVGcanvas method in ProEpilogue class
    
    genArt(numShapes, f, 2) # generate art using genArt method
    
    ProEpi.closeSVGcanvas(f, 1) # close SVG canvas using closeSVGcanvas method in ProEpilogue class
    
    f.close() # close file
    
def main():
    '''main method'''
     
    num_shapes = 10000 # number of shapes we want in the artwork, more will make the image more full of shapes and colourful!
    
    writeHTMLfile(num_shapes) # write HMTL file with the number of shpaes stated 
        
main()