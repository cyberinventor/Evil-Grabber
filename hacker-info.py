import os
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import platform
import requests
import time
import sys
import keyboard
import threading
import pyfiglet
from pyfiglet import Figlet

class banner():
    """For Beginners new to coding and want to experiment or learn
    from my code the values are down below
    """
    red = "\u001b[31m"
    green = "\u001b[32m"
    yellow = "\u001b[33m"
    blue = "\u001b[34m"
    reset = "\u001b[0m"
    
    banner = """
\u001b[31m
█░█ ▄▀█ █▀▀ █▄▀ █▀▀ █▀█   █ █▄░█ █▀▀ █▀█
█▀█ █▀█ █▄▄ █░█ ██▄ █▀▄   █ █░▀█ █▀░ █▄█

[\u001b[0m 1 \u001b[31m] \u001b[0m gather phoneinfo\u001b[31m
[\u001b[0m 2 \u001b[31m] \u001b[0m text to ascii art\u001b[31m
\nplatform: \u001b[0mwindows\u001b[31m
    """
    if platform.system() == str("Windows"):
        os.system("cls")
        print(banner)
    elif platform.system() == "Darwin":
        os.system("clear")
        print(banner.replace("windows", "darwin"))
    elif platform.system() == "Linux":
        os.system("clear")
        print(banner.replace("windows", "linux"))

def banner_plaform():
    if platform.system() == str("Windows"):
        print(banner().banner)
    elif platform.system() == str("Linux"):
        print(banner().banner.replace("windows", "linux"))
    elif platform.system() == str("Darwin"):
        print(banner().banner.replace("windows", "darwin"))



def evil():
    try:
        while True:
            banner()
            options = input("option: ")
            if options == str("1"):
                print("to go back to the home screen press: q")
                phonenumber = input("phonenumber: ")
                if keyboard.is_pressed("q"):
                    os.system("python evilgrabber.py")
                
                phone = phonenumbers.parse("+"+phonenumber)
                time_zone = timezone.time_zones_for_number(phone)
                carrier_name = carrier.name_for_number(phone, 'en')
                region = geocoder.description_for_number(phone, 'en')
                valid = phonenumbers.is_valid_number(phone)
                possible = phonenumbers.is_possible_number(phone)

                try:
                    r = requests.get(f"https://truecaller.shadowbrokers.repl.co/?phonenumber={phonenumber}&get_info=Submit")
                    r = requests.get("https://truecaller.shadowbrokers.repl.co/output.txt")
                    print(f"""
\u001b[34m[ \u001b[32m{phone} \u001b[34m]
\u001b[34m[ \u001b[32mTimezone: {time_zone} \u001b[34m]
\u001b[34m[ \u001b[32mCarrier: {carrier_name} \u001b[34m]
\u001b[34m[ \u001b[32mRegion: {region} \u001b[34m]
\u001b[34m[ \u001b[32mValid: {valid} \u001b[34m]
\u001b[34m[ \u001b[32mPossible: {possible} \u001b[34m]
\u001b[33m
{r.text}
\u001b[32mwrote results to results.txt\u001b[31m
""")
                    f = open("results.txt", "a")
                    f.write(f"""[ {phone} ]
[ Timezone: {time_zone} ]
[ Carrier: {carrier_name} ]
[ Region: {region} ]
[ Valid: {valid} ]
[ Possible: {possible} ]
obtaining more info
{r.text}\n
""")
                    f.close()
                    if platform.system() == str("Windows"):
                        print(banner().banner)
                    elif platform.system() == str("Linux"):
                        print(banner().banner.replace("windows", "linux"))
                    elif platform.system() == str("Darwin"):
                        print(banner().banner.replace("windows", "darwin"))

                except (requests.ConnectionError, requests.Timeout) as exception:
                    print(f"""
\u001b[34m[\u001b[32m {phone} \u001b[34m]
\u001b[34m[\u001b[32m Timezone: {time_zone} \u001b[34m]
\u001b[34m[\u001b[32m Carrier: {carrier_name} \u001b[34m]
\u001b[34m[\u001b[32m Region: {region} \u001b[34m]
\u001b[34m[\u001b[32m Valid: {valid} \u001b[34m]
\u001b[34m[\u001b[32m Possible: {possible} \u001b[34m]
\u001b[33mobtaining more info
Unable to obtain more info no internet access\u001b[33m

\u001b[32mwrote results to results.txt\u001b[31m
""")
                    f = open("results.txt", "a")
                    f.write(f"""[ {phone} ]
[ Timezone: {time_zone} ]
[ Carrier: {carrier_name} ]
[ Region: {region} ]
[ Valid: {valid} ]
[ Possible: {possible} ]
obtaining more info
Unable to obtain more info no internet access
""")
                    f.close()
                    if platform.system() == str("Windows"):
                        print(banner().banner)
                    elif platform.system() == str("Linux"):
                        print(banner().banner.replace("windows", "linux"))
                    elif platform.system() == str("Darwin"):
                        print(banner().banner.replace("windows", "darwin"))
            elif options == "2":
                text = input("enter the text to convert:\u001b[0m ")
                #result = pyfiglet.figlet_format(text)
                #print(f"\u001b[31m{result}")
                result = pyfiglet.figlet_format(text, font="banner3-D")
                print(result)
                banner_plaform()
                
    except KeyboardInterrupt:
        if platform.system() == str("Windows"):
            os.system("echo %username% > .user.txt")
            f = open(".user.txt")
            print(f"\nExiting Bye Bye \u001b[32m{f.read()}\u001b[31m"+ "Love you i am your computer")
            f.close()
            os.remove(".user.txt")
        else:
            os.system("echo $USER > .user.txt")
            f = open(".user.txt")
            print(f"\nExiting Bye Bye \u001b[32m{f.read()}\u001b[31m"+ "Love you i am your computer\u001b[0m")
            f.close()
            os.remove(".user.txt")
        print("\u001b[0m")
        sys.exit()
evil()
