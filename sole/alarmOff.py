#!/usr/bin/env python
from alarmHandler import AlarmHandler

# Cron Job to turn off alarm -- no alarm will be set
def main():
    alarmHandler = AlarmHandler()
    alarmHandler.off()

if __name__ == "__main__":
    main()