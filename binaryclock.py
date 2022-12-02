#!/usr/bin/env python
import colours, displays, controls #disse er ting, jeg selv har strikket sammen.
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time, datetime, signal, sys


hat = SenseHat() #så behøver vi ikke at skrive "SenseHat" hele tiden, smart!


clockLoop = True #Denne skal bruges til det overordnede loop. Når dette bliver False skal programmet slutte.
messageCounter = True #Denne counter har kun til formål at sikre, at vi ikke viser startbesked flere gange
clockMode = 1 #Skal bruges til at vælge mellem de fire visningsmuligheder for uret.
hat.clear() #Sætter alle dioder til 0,0,0/slukket
x, y = 0, 7 #Skal bruges til indikator for AM/PM
msgSpeed = 0.04 #bruges til at justere beskedhastighed

amPm = 12 #Bruges i stedet for at have hardcoded "12", for at demonstrere AM/PM-funktion



while clockLoop == True:
    while messageCounter == True:
        hat.show_message("Programmet starter", scroll_speed=msgSpeed)#Startbesked jf. formalia. Så langt, så godt.
        messageCounter = False #Vi kører kun denne én gang.        

    for event in hat.stick.get_events(): #her vælger vi konkret mellem de fire(fem) muligheder        
        if event.direction =="left": clockMode = 1 
        elif event.direction == "right": clockMode = 2
        elif event.direction =="up": clockMode = 3
        elif event.direction == "down": clockMode = 4
        elif event.direction == "middle": #Trykker man direkte ned på joysticket slukker vi programmet.
            hat.show_message("Programmet slutter", scroll_speed= msgSpeed)
            signal.signal(signal.SIGTERM)            
            clockLoop = False
        hat.clear()
        
    if clockMode == 1: #Når vi starter kører vi "enere og tiere" samlet, og tiden horisontal.  ### DONE
        t = datetime.datetime.now() #Her henter vi den konkrete tid frem.
        

        hat.set_pixel(x, y, colours.off)
        displays.displayRow(t.hour, 1, colours.hourColour)      #Timer på placering "1" (i virkeligheden 2, da det starter ved 0)
        displays.displayRow(t.minute, 3, colours.minuteColour)  #Jeg vælger at have en rækkes mellemrum, for overskuelighedens skyld.
        displays.displayRow(t.second, 5, colours.secondColour)  #Samme her.
        
        if clockLoop == False:
            break        #Her breaker vi, så vi kan få slukket programmet.
                    

    elif clockMode == 2: #Når vi vælger clockMode 2 vil vi vise klokken vertikalt i stedet for horisontalt, og opdelt i to tal pr tal. Ellers som 1.
    #    while clockMode == 2:
        hat.set_pixel(x, y, colours.off)    #Bruges til at cleare evt. AM/PM-indikatorpixel
        t = datetime.datetime.now()

        hoursTens = t.hour // 10    #Dette foretages for at splitte hele tiere fra énere (0, 1 og 2 mulig)
        hoursOnes = t.hour % 10     #Modulus 10 viser os restproduktet efter vi har fjernet hele tiere.
        minTens = t.minute // 10
        minOnes = t.minute % 10
        secTens = t.second //10
        secOnes = t.second % 10

        displays.displayColumn(hoursTens, 1, colours.hourColour)
        displays.displayColumn(hoursOnes, 2, colours.hourColour)
        displays.displayColumn(minTens, 3, colours.minuteColour)
        displays.displayColumn(minOnes, 4, colours.minuteColour)
        displays.displayColumn(secTens, 5, colours.secondColour)
        displays.displayColumn(secOnes, 6, colours.secondColour)        


    elif clockMode == 3: #som 1, men AM/PM.
        #while clockMode == 3:
        x, y = 0, 7 #Skal bruges til indikator for AM/PM
        t = datetime.datetime.now()
        if (t.hour > amPm):   #Hvis tiden klokken er 13 eller derover, trækker vi 12 fra tiden og tænder en indikatorpixel
            displays.displayRow(t.hour - amPm, 1, colours.hourColour)
            hat.set_pixel(x, y, colours.papayaWhip)
        else:
            displays.displayRow(t.hour, 1, colours.hourColour) #Er klokken ikke over 13, så skal indikatorpixlen slukkes.
            hat.set_pixel(x, y, colours.off)                  #Man kunne også have gået med to forskellige farvesæt.
        displays.displayRow(t.minute, 3, colours.minuteColour)
        displays.displayRow(t.second, 5, colours.secondColour)        


    elif clockMode == 4: #Når vi vælger clockMode 4 vil vi se det samme som #2, men med AM/PM
        x, y = 0, 7 #Skal bruges til indikator for AM/PM
        t = datetime.datetime.now()

        hoursTens = t.hour // 10 #Dette foretages for at splitte hele tiere fra énere (0, 1 og 2 mulig)
        hoursOnes = t.hour % 10 #Modulus 10 viser os restproduktet efter vi har fjernet hele tiere.
        minTens = t.minute // 10
        minOnes = t.minute % 10
        secTens = t.second //10
        secOnes = t.second % 10

        if (t.hour > amPm): #Er antal timer højere end 12 skal vi trække 12 fra. Den skal aldrig vise "0" eller noget højere end 12.
            displays.displayColumn((t.hour - amPm)//10, 1, colours.hourColour)
            displays.displayColumn((t.hour - amPm)%10, 2, colours.hourColour)
            hat.set_pixel(x, y, colours.papayaWhip)
        else:
            displays.displayColumn(hoursTens, 1, colours.hourColour)
            displays.displayColumn(hoursOnes, 2, colours.hourColour)
            hat.set_pixel(x, y, colours.off)
        displays.displayColumn(minTens, 3, colours.minuteColour)
        displays.displayColumn(minOnes, 4, colours.minuteColour)
        displays.displayColumn(secTens, 5, colours.secondColour)
        displays.displayColumn(secOnes, 6, colours.secondColour)

    time.sleep(1)