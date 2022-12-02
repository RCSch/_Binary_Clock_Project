"""
Colours bruger til at styre farverne. 
Der er angivet farver for tidsenheder:
hourColour      : bruges til timer
minuteColour    : bruges til minutter
secondColour    : bruges til sekunder 

Endvidere er der angivet to øvrige farver:
off             : bruges til at slukke individuelle dioder.
papayaWhip      : bruges til AM/PM-indikator. 

Der er også lavet et sæt farver til PM-brug.
Disse kan bruges til at holde et anderledes farvetema om eftermiddagen.
Dette kunne være et alternativ til at have en AM/PM-bit.
Dette er dog på nuværende tidspunkt ikke implementeret, da det virker på opgavebeskrivelsen som om de hellere vil ha' en bit.
"""

hourColour = (255, 0, 0) #Rød (1)
"""blablabla """
minuteColour = (255, 255, 255) #Hvid (2)
secondColour = (0,0,255) #Blå (3)

off = (0, 0, 0) #Denne bruges til at slukke for dioder.
papayaWhip = (255,239,213) #Farve til AM/PM-indikator


hourPM = (100, 255, 100)
minutePM=(150, 150, 255) 
secondPM=(255,75,75)



