import sys
import math
from tkinter import *

if len(sys.argv) < 2:
    print("No file name\n")
    sys.exit(1)

width = 0
height = 0

pixelMap = []


class Pixel:
    r = 0
    g = 0
    b = 0

    def __init__(self, red, green, blue):
        self.r = red
        self.g = green
        self.b = blue

    def toHexString(self):
        return "#" + hex(self.r)[2:3]+hex(self.g)[2:3]+hex(self.b)[2:3]


with open(sys.argv[1], "rb") as file:
    header = file.read(14)
    if(header[0] != 66) or (header[1] != 77):
        print("Wrong header\n")
        sys.exit(1)
    dibStr = file.read(4)
    dibSize = 0
    for i in range(0, 4):
        dibSize = dibSize + dibStr[i]*(256**i)

    dib = file.read(dibSize-4)
    for i in range(0, 4):
        width = width + dib[i]*(256**i)
    for i in range(0, 4):
        height = height + dib[i+4]*(256**i)
    print(str(width)+"x"+str(height))
    for y in range(0, height):
        row = []
        for x in range(0, width):
            pixel = file.read(3)
            row.append(Pixel(pixel[2], pixel[1], pixel[0]))
        pixelMap.append(row)

window = Tk()
can = Canvas(window, width=width, height=height)
for y in range(0, height):
    for x in range(0, width):
        can.create_rectangle(
            (x, height-y)*2, fill=pixelMap[y][x].toHexString(), outline="")
can.pack()
mainloop()
