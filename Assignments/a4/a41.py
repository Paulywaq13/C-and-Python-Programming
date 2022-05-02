#!/usr/bin/env python3
'''Assignment 4 Part 1'''
print(__doc__)

from typing import IO

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
        
def genArt(f: IO[str], t: int) -> None:
    '''genART method'''
   
    # create a circle line in html file
    drawCircleLine(f, t, Circle((50,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((150,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((250,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((350,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((450,50,50), (255,0,0,1.0)))
    drawCircleLine(f, t, Circle((50,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((150,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((250,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((350,250,50), (0,0,255,1.0)))
    drawCircleLine(f, t, Circle((450,250,50), (0,0,255,1.0)))
   
    # create a rectangle line in html file
    drawRectangleLine(f, t, Rectangle((550,0,50,100), (0,255,0,1.0)))
    drawRectangleLine(f, t, Rectangle((650,0,50,100), (0,255,0,1.0)))
    drawRectangleLine(f, t, Rectangle((750,0,50,100), (0,255,0,1.0)))
    drawRectangleLine(f, t, Rectangle((850,0,50,100), (0,255,0,1.0)))
    drawRectangleLine(f, t, Rectangle((950,0,50,100), (0,255,0,1.0)))
    drawRectangleLine(f, t, Rectangle((550,200,50,100), (255,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((650,200,50,100), (255,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((750,200,50,100), (255,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((850,200,50,100), (255,0,255,1.0)))
    drawRectangleLine(f, t, Rectangle((950,200,50,100), (255,0,255,1.0)))
            


def writeHTMLline(f: IO[str], t: int, line: str) -> None:
     '''writeLineHTML method'''
     ts = "   " * t
     f.write(f"{ts}{line}\n")
     

def writeHTMLfile():
    '''writeHTMLfile method'''
    fnam: str = "a41.html"
    winTitle = "My Art"
    
    f: IO[str] = open(fnam, "w")
    
    ProEpi = ProEpilogue()
    
    ProEpi.writeHTMLHeader(f, winTitle)
    
    ProEpi.openSVGcanvas(f, 0, (1000,1000))
    
    genArt(f, 2)
    
    ProEpi.closeSVGcanvas(f, 1)
    
    f.close()

def main():
    '''main method'''
    writeHTMLfile()

main()

                                                                                                                                                                                                                                                                                                        
