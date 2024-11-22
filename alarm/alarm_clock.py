#pip install playsound
#si no lo acepta entonces: pip install --upgrade wheel. luego el primer paso
from playsound import playsound
import time
import os

os.system("")

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

def alarm(seconds):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed+=1
        
        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN} Sonara en: {minutes_left:02d}:{seconds_left:02d}")
        
    playsound("alarm.mp3")
        
minutes = int(input("Cuantos minutos: "))
seconds = int(input("Cuantos segundos: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds)