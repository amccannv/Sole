import datetime, os
from crontab import CronTab

# This class will handle scheduling and unscheduling cron jobs on the OS.
class AlarmScheduler(object):

    def __init__(self):
        self.cron = CronTab(user = True)

    def scheduleAlarm(self, hour, minute):

        # Unschedule old alarm - will replace with new alarm
        self.cron.remove_all(comment = 'ON')

        # Create new alarm
        currentDir = os.path.abspath(\
            os.path.dirname(os.path.realpath(__file__)))
        onJob = self.cron.new(command = currentDir + '/alarmOn.py', comment = 'ON')

        # Set alarm time
        onJob.minute.on(minute)
        onJob.hour.on(hour)
        self.cron.write()

        return True

    def turnOffAlarm(self):

        # Unschedule old alarm
        self.cron.remove_all(comment = 'ON')
        self.cron.write()
        return True