import feedparser
link='https://emergencyalert.alberta.ca/aea/feed.rss'
#link='feed.rss' # FOR TESTING PURPOSES (saved from the system test on November 28, 2018)
import time
import pyttsx3
import os
from playsound import playsound

engine = pyttsx3.init()
engine.setProperty('rate',125)
print('initiated alert system')
def is_alert(link,x):
    try:
        alert = feedparser.parse(link).entries[x].title
    except:
        return(0)
def alert():
    x = 0
    while True:
        if(is_alert(link,x) != 0):
            x+=1
            continue
        else:
            return(x)
            break        
while True:
        alerts = alert()
        for x in range(alerts):
            start = feedparser.parse(link).entries[x].title
            os.system('nircmd setvolume 0 65535 0')
            print("ALERT RECIEVED")
            print(start)
            playsound('alert.mp3')
            engine.say('AN EMERGENCY ALERT HAS BEEN RECEIVED')
            engine.runAndWait()
            time.sleep(0.5)
            engine.say(start)
            engine.runAndWait()
            engine.say(feedparser.parse(link).entries[x].description)
            engine.runAndWait()
            os.system('nircmd setvolume 0 0 0')
        time.sleep(5)
