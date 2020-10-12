import os
import phonenumbers
from phonenumbers import timezone, geocoder, carrier
import platform
import requests
import time
import sys

def check():
    url = "http://www.kite.com"
    timeout = 5
    f = open(".connection.txt", "w")
    try:
        request = requests.get(url, timeout=timeout)
        print("Connected to the Internet")
        f.write("Connected")
    except (requests.ConnectionError, requests.Timeout) as exception:
        print("No internet connection.")
        f.write("Not connected")
check()
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
    
█▀▀ █░█ █ █░░   █▀▀ █▀█ ▄▀█ █▄▄ █▄▄ █▀▀ █▀█
██▄ ▀▄▀ █ █▄▄   █▄█ █▀▄ █▀█ █▄█ █▄█ ██▄ █▀▄


[\u001b[0m 1 \u001b[31m] \u001b[0m gather phoneinfo\u001b[31m
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
    
def evil():
    try:
        while True:
            banner()
            options = input("option: ")
            if options == str("1"):
                phonenumber = input("phonenumber: ")

                phone = phonenumbers.parse("+"+phonenumber)
                time_zone = timezone.time_zones_for_number(phone)
                carrier_name = carrier.name_for_number(phone, 'en')
                region = geocoder.description_for_number(phone, 'en')
                valid = phonenumbers.is_valid_number(phone)
                possible = phonenumbers.is_possible_number(phone)
            
                print(f"""
\u001b[34m[\u001b[32m {phone} \u001b[34m]
\u001b[34m[\u001b[32m Timezone: {time_zone} \u001b[34m]
\u001b[34m[\u001b[32m Carrier: {carrier_name} \u001b[34m]
\u001b[34m[\u001b[32m Region: {region} \u001b[34m]
\u001b[34m[\u001b[32m Valid: {valid} \u001b[34m]
\u001b[34m[\u001b[32m Possible: {possible} \u001b[34m]
\u001b[33mobtaining more info\u001b[33m
""")
                r = requests.get(f"https://truecaller.shadowbrokers.repl.co/?phonenumber={phonenumber}&get_info=Submit")
                f = open(".connection.txt")
                if (f.read() == "Connected"):
                    if r.status_code == 200:
                        r = requests.get(f"https://truecaller.shadowbrokers.repl.co/output.txt")
                        print(r.text, "\u001b[31m")
                        f = open("results.txt", "a")
                        f.write(f"""Date: {time.ctime()}
[ {phone} ]
[ Timezone: {time_zone} ]
[ Carrier: {carrier_name} ]
[ Region: {region} ]
[ Valid: {valid} ]
[ Possible: {possible} ]
obtaining more info
{r.text}\n
""")
                        f.close()
                        print("\u001b[32mwrote info in results.txt\u001b[31m")
                        if platform.system() == "Windows":
                            print(banner().banner)
                        elif platform.system() == "Darwin":
                            print(banner().banner.replace("windows", "darwin"))
                        elif platform.system() == "Linux":
                            print(banner().banner.replace("windows", "linux"))

                        f.close()
                        os.remove(".connection.txt")
                elif (f.read() == "Not connected"):
                    print("""[ Timezone: {time_zone} ]
[ Carrier: {carrier_name} ]
[ Region: ]
[ Valid: {valid} ]
[ Possible: {possible} ]
obtaining more info internet not connected""")
                    f = open("results.txt", "a")
                    f.write(f"""Date: {time.ctime()}
[ {phone} ]
[ Timezone: {time_zone} ]
[ Carrier: {carrier_name} ]
[ Region: ]
[ Valid: {valid} ]
[ Possible: {possible} ]
obtaining more info internet not connected so cannot obtain more info
""")
                    f.close()
                    if platform.system() == "Windows":
                        print(banner().banner)
                    elif platform.system() == "Darwin":
                        print(banner().banner.replace("windows", "darwin"))
                    elif platform.system() == "Linux":
                        print(banner().banner.replace("windows", "linux"))
                    os.remove(".connection.txt")
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
