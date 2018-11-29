# AlbertaEmergencyAlerts
A RSS Feed Bot with TTS to notify in the case of an emergency.

# Full Disclaimer
This program is designed to help those who are not consistantly connected to an LTE network recieve Alberta Emergency Alerts.
While great care has been taken to ensure that the program runs consistantly, it can NOT be guarenteed to work in the event of an emergency alert. As well, the Author will not take any responsibility in the case of malfunction at a critical time. 

## Customizable Features
While this program is designed to work with the [Alberta Emergency Alert](https://www.emergencyalert.alberta.ca/) system, it is possible for the feed to be changed to your local system. The link should be an rss feed with the format being of the [Net Alert](http://www.netalerts.org/cap-feed.html) standard.

One may wish to change the sound file to the final countdown or Never Gonna Give You Up. Simply change the alert.mp3 sound file.

## Requirements:
```python
pip install feedparser
pip install pyttsx3
pip install playsound
```

For Windows: [nirsoft](http://www.nirsoft.net/utils/nircmd.html)

Alternative programs can be used by modifying the os.system() command. 
