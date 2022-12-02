# from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED 
# #Som det ser ud eftermiddag 29.11. bruger vi ikke ACTION_PRESSED. Det er måske foruroligende.
# from signal import pause
# import time, datetime #Måske? bruges ikke konkret her. ENDNU!

# hat = SenseHat()

# # def pushed_left(event): #Tanken er, at vi skifter clockMode ved at slippe joysticket, efter at vi har peget i en eller anden retning.
# #     global clockMode
# #     if event.action != ACTION_RELEASED:
# #         clockMode = 1
        

# # def pushed_right(event):
# #     global clockMode
# #     if event.action != ACTION_RELEASED:
# #         clockMode = 2
        

# # def pushed_up(event):
# #     global clockMode
# #     if event.action != ACTION_RELEASED:
# #         clockMode = 3
        

# # def pushed_down(event):
# #     global clockMode
# #     if event.action != ACTION_RELEASED:
# #         clockMode = 4
        

# # def refresh():
# #     hat.clear() #Bruger jeg nogensinde denne her? Hvem ved
# def joystick(clockMode, clockLoop, event):
#     for event in hat.stick.get_events():
#         if event.direction =="left": clockMode = 1
#         elif event.direction == "right": clockMode = 2
#         elif event.direction =="up": clockMode = 3
#         elif event.direction == "down": clockMode = 4
#         elif event.direction == "middle":
#             hat.show_message("Programmet slutter", scroll_speed= 0.1)
#             hat.clear()
#             clockLoop = False
#         hat.clear()
#     return clockMode, clockLoop
#     #time.sleep(1)




