# colors values 
Red = '\033[1;31m'
Blue= '\033[1;36m'
Endc = '\033[0m'
import subprocess
import sys
import os
import webbrowser
verl = open("core/.version", 'r').read()
line = '--------------------------------------------'

def clr():
    try:
        if os.name == "nt":
            os.system('cls')
        else :
            os.system('clear')
    except:
        pass       


def banner():
    clr()
    logo="""
 ██░ ██  ██▓███   ▒█████   ███▄ ▄███▓ ▄▄▄▄   
▓██░ ██▒▓██░  ██▒▒██▒  ██▒▓██▒▀█▀ ██▒▓█████▄ 
▒██▀▀██░▓██░ ██▓▒▒██░  ██▒▓██    ▓██░▒██▒ ▄██
░▓█ ░██ ▒██▄█▓▒ ▒▒██   ██░▒██    ▒██ ▒██░█▀  
░▓█▒░██▓▒██▒ ░  ░░ ████▓▒░▒██▒   ░██▒░▓█  ▀█▓
 ▒ ░░▒░▒▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒░   ░  ░░▒▓███▀▒
 ▒ ░▒░ ░░▒ ░       ░ ▒ ▒░ ░  ░      ░▒░▒   ░ 
 ░  ░░ ░░░       ░ ░ ░ ▒  ░      ░    ░    ░ 
 ░  ░  ░             ░ ░         ░    ░      
                                           ░ 


               ""","""
----------------   ----------------------
| KLS  Project |   | Version : """,verl,""" |
----------------   ----------------------

\tCreated by Honey Pots...

-------------------------------------------- """
    print(Red+logo[0]+Blue+logo[1]+logo[2]+logo[3])
    print(Red +"""            [ Main Menu ] \n"""+ Blue + """
        
[01] Instagram I'D : honeypots0
[02] Twitter I'D : honeypots0
[03] Youtube Channel : Honey Pots 
[04] Back 
""")
    x = input('Press any Enter For Back : ')
    subprocess.call([sys.executable, 'hpomb.py'])
banner()