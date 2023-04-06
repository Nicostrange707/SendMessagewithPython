import pyautogui as pt
import time

limit = input("Anzahl der Nachrichten: ")
message = input("Nachricht:")
i=0

time.sleep(3)

if limit<500:
while i<int(limit):
    pt.typewrite(message)
    pt.press("enter")
    
    i+=1
    
elif:
    exit()
