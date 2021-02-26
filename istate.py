#!/usr/bin/env python3
import datetime
from os import system
from sys import argv, platform
from time import sleep

# Usage: python3 istate.py <optional: delay between each ping test, default: 5>
WAIT_TIME = int(argv[1]) if len(argv) > 1 else 5

try:
    while True:
        ping_response = system("ping google.com -c 4 -t 3 1> /dev/null")

        if ping_response == 0:
            print(datetime.datetime.now().strftime("%H:%M:%S"), "up")
            # For macOS. With system voice, say 'Internet is up.'
            if platform == 'darwin': system("say internet is up.")
        else:
            print(datetime.datetime.now().strftime("%H:%M:%S"), "down")
            # say 'Internet is down.'
            if platform == 'darwin': system("say internet is down.")

        sleep(WAIT_TIME)

except KeyboardInterrupt:
    print("🏃‍♂️ Exiting.")
    exit(0)
