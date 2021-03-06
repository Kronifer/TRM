#! /usr/bin/python3.7

import kvJSON as kv
import os

def menuscreen():
    print("""
    Welcome to TRM alpha!          Not logged in. Please type r to register or l to login.
    
    a) Play Angband                b) Play Unangband

    c) Play CDDA                   d) Play Dungeon Crawl: Stone soup

    e) Play Nethack                r) Register

    l) Login\n""")

def setpass():
    password = input("Set your password. These are case-sensitive! ")
    print("\n")
    passConfirm = input("You have chosen your password to be: " + password + " . Is that okay? [y/n] ")
    if passConfirm == 'y':
        kv.addData("password", password)
        kv.encryptData("password")
    else:
        setpass()

def init():
    kv.init("data.json")
    check = kv.getData("gamelist")
    if check == None:
        config = input("It seems you have not configured TRM yet. Would you like to now? If no, TRM will be autoconfigured. [y/n] ")
        print("First, you need to decide what games you want users to play.\n")
        print("""Here is a list of current supported games:
        a: Cataclysm: Dark Days Ahead
        b: Angband
        c: Unangband
        d: Dungeon Crawl: Stone Soup
        e: Nethack\n
        """)
        gameList = input("""To choose the games you want people to be able to play, please
enter the letter corresponding with the games people can play in a list like so: 
abc, where each character is unseparated. """)
        os.system("clear")
        kv.addData("gamelist", gameList)
        print("TRM will now install these programs. \n")
        for element in gameList:
            if element == "a":
                os.system("sudo apt install cataclysm-dda-curses")
            elif element == "b":
                os.system("sudo apt install angband")
            elif element == "c":
                os.system("git clone --depth=1 https://github.com/DGoldDragon28/Unangband/")
                os.system("cd Unangband/src")
                os.system("sudo make -f Makefile.std install")
                os.system("cd ..")
            elif element == "d":
                os.system("echo 'deb https://crawl.develz.org/debian crawl 0.26' | sudo tee -a /etc/apt/sources.list")
                os.system("wget https://crawl.develz.org/debian/pubkey -O - | sudo apt-key add -")
                os.system("sudo apt-get update")
                os.system("sudo apt install crawl-common=0.25.0-1")
                os.system("sudo apt-get install crawl")
            else:
                os.system("sudo apt install nethack-console 3.6.1-1")
                os.system("clear")
                print("Games installed.\n")
                setpass()
                os.system("clear")
                print("Congratulations! TRM is configured.")

    else:
        adminPass = kv.getData("password")
        gamelist = kv.getData("gamelist")
        gamelistlist = []
        for element in gamelist:
            element += gamelistlist

def main():
    menuscreen()
    command = input()
    

                


init()
    