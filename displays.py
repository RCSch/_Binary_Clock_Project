"""Der er defineret to display typer: 

displayRow til horisontal urvisning

displayColumn til vertikal urvisning"""

from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED 
from signal import pause #pause bliver ikke pt brugt
import colours
#Her har jeg defineret fire forskellige display-setups.  Jeg kunne i virkeligheden have nøjedes med to.

hat = SenseHat() 
off = (0, 0, 0) #til at slukke dioder med.

def displayRow(value, row, color): #Denne er sat op til horisontal visning.
    binary_str = "{0:8b}".format(value) #Binary string gives maxværdi 8, da der kun er otte rækker/kolonner i displayet
    for x in range(0, 8):
        if binary_str[x] == '1': #Dersom værdien er 1, skal lyset tændes.
            hat.set_pixel(x, row, color)
        else: #Er værdien ikke 1, skal skidtet slukkes.
            hat.set_pixel(x, row, off)


def displayColumn(value, column, color): #til vertikal visning.
     binary_str = "{0:8b}".format(value) 
     for y in range(0, 8):
         if binary_str[y] == '1': 
             hat.set_pixel(column, y, color)
         else:
             hat.set_pixel(column, y, off)

