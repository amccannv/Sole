import datetime
import os
import random

from flask import Flask
from lightHandler import LightHandler
from sundownHandler import SundownHandler
from scheduler import AlarmScheduler

# Global Variables
wakeUpTime = '0:30'
alarmSet = False
wakeUpColour = (30, 30, 30)
sleepTimeSet = False
sleepTimeColour = (30, 30, 30)
customLightSet = False
customColour = (30, 30, 30) # rgb values, 0-255 -- to be reviewed after LED strips arrive

# Handlers and alarm scheduler
lightHandler = LightHandler()
sundownHandler = SundownHandler()
alarmScheduler = AlarmScheduler()


app = Flask(__name__)

# Main Index
@app.route('/')
def index():
    return 'What up this my Sole server'


## Wake Up Pattern

# Change wake-up time
@app.route('/setWakeUp/<newWakeUpTime>')
def setWakeUp(newWakeUpTime):
    wakeUpTime = newWakeUpTime
    hour, minute = wakeUpTime.split(":")
    alarmScheduler.scheduleAlarm(hour, minute)
    alarmSet = True
    return 'Alarm Set for ' + wakeUpTime

# Change custom colour for alarm
@app.route('/setWakeUpColour/<customColour>')
def setWakeUpColour(customColour):
    customColour = customColour
    print('New wake up colour is ' + customColour)
    return 'New wake up colour is ' + customColour

# Turn off alarm
@app.route('/turnOffAlarm')
def turnOffAlarm():
    alarmScheduler.turnOffAlarm()
    alarmSet = False
    print('Alarm is set to be off')
    return 'Alarm is set to be off'


## Sleep Time Pattern

# Change sleep time colour
@app.route('/setSleepTimeColour/<customColour>')
def setSleepTimeColour(customColour):
    sleepTimeColour = customColour
    print('New sleep time colour is ' + customColour)
    return 'New sleep time colour is ' + customColour

# Turn custom light on
@app.route('/turnOnSleepTime')
def turnOnSleepTime():
    sundownHandler.on(sleepTimeColour)
    sleepTimeSet = True
    print('Sleep time cycle is on')
    return 'Sleep time cycle is on'

# Turn custom light off
@app.route('/turnOffSleepTime')
def turnOffSleepTime():
    sundownHandler.off()
    sleepTimeSet = False
    print('Sleep time cycle is off')
    return 'Sleep time cycle is off'


## Custom Light

# Change custom colour for light
@app.route('/setCustomColour/<customColour>')
def setCustomColour(customColour):
    customColour = customColour
    print('New custom colour is ' + customColour)
    return 'Custom colour is ' + customColour

# Turn custom light on
@app.route('/turnOnCustomLight')
def turnOnCustomLight():
    lightHandler.on(customColour)
    customLightSet = True
    print('Custom colour light is on')
    return 'Custom colour light is on'

# Turn off custom light
@app.route('/turnOffCustomLight')
def turnOffCustomLight():
    lightHandler.off()
    customLightSet = False
    print('Custom colour light is off')
    return 'Custom colour light is off'

## Main Code

def main():
    app.run(debug = True, host = '0.0.0.0')

if __name__ == '__main__':
    main()
