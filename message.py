import pyautogui as pt
import time

print("Message Limit set to 500")
limit = input("Anzahl der Nachrichten: ")
message = input("Nachricht:")
i=0

time.sleep(3)

if limit<500:
    while i<int(limit):
     pt.typewrite(message)
     pt.press("enter")
    
    i+=1
    
else:
    exit()
