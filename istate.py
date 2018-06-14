#!/usr/bin/env python3
from os import system
from time import sleep
from sys import argv, platform

try:
	while True:
		x = system('ping google.com -c 4 -t 3')
		
		if x == 0:
			print("up")
			#if platform == 'darwin': system("say internet is up")
		else:
			print("down")
			#if platform == 'darwin': system("say internet is down")
		
		sleep(int(argv[1]) if len(argv) > 1 else 27)

except KeyboardInterrupt:
	print()
	exit(0)
#sat dec 16 4:11 pm