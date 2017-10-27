#Author : Shashank Srivastava
#Date : 27th of October, 2017
from pync import Notifier
import subprocess
def notify(text):
    Notifier.notify(text)
COMMAND = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | grep SSID | tail -1 | awk '{print $2}'"
SSID = subprocess.check_output(COMMAND,shell = True).decode("utf-8").strip()
print("You are connected to : " + SSID)
notify("You are connected to : \n" + SSID)
