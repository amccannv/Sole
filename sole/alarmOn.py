#!/usr/bin/env python
from sunriseHandler import SunriseHandler

# Cron Job to turn on alarm sequence
def main():
    sunriseHandler = SunriseHandler()
    sunriseHandler.on()

if __name__ == "__main__":
    main()