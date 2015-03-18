'''
    @author: lesspion
'''
import time
from datetime import datetime
import os
import time
import wave
import sys

alarm = "heure-min";
curHour = int(time.strftime("%H", time.gmtime())) + 1
curMinutes = time.strftime("%M", time.gmtime())
curSeconds = time.strftime("%S", time.gmtime())
print(str(curHour) + ":" + str(curMinutes) + ":" + str(curSeconds))
while(str(curHour) + ":" + str(curMinutes) + ":" + str(curSeconds) != "23:48:10"):
    time.sleep(1)
    curHour = int(time.strftime("%H", time.gmtime())) + 1
    curMinutes = time.strftime("%M", time.gmtime())
    curSeconds = time.strftime("%S", time.gmtime())
    print(str(curHour) + ":" + str(curMinutes) + ":" + str(curSeconds))

os.startfile('Rengar le Chat - Remix de la nouvelle daube de Corobizar.mp3')
