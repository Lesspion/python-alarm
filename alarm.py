'''
    @author: lesspion
'''
import time
from datetime import datetime
import os
import time
import wave
import sys
import platform

print(sys.platform)
alarm = "heure-min";
curHour = int(time.strftime("%H", time.gmtime()))
curMinutes = time.strftime("%M", time.gmtime())
curSeconds = time.strftime("%S", time.gmtime())
print(str(curHour) + ":" + str(curMinutes) + ":" + str(curSeconds))
while(str(curHour) + ":" + str(curMinutes) + ":" + str(curSeconds) != "23:50:00"):
    time.sleep(1)
    curHour = int(time.strftime("%H", time.gmtime()))
    curMinutes = time.strftime("%M", time.gmtime())
    curSeconds = time.strftime("%S", time.gmtime())
    print(str(curHour) + ":" + str(curMinutes) + ":" + str(curSeconds))


#os.startfile('Rengar le Chat - Remix de la nouvelle daube de Corobizar.mp3')

if (sys.platform == "linux"):
	os.system('vlc ~/Musique/FNAF.mp3')
else:
	os.startfile('~/Musique/lightbringer.mp3')
