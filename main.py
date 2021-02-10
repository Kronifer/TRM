#! /usr/bin/python3.7

import kvJSON as kv
import os

def init():
    kv.init("data.json")
    check = kv.getData("gamelist")
    if check == None:
        config = input("It seems you have not configured TRM yet. Would you like to now? If no, TRM will be autoconfigured. [y/n] ")
        if config == "y":
            os.system("clear")
            print("First, you need to decide what games you want users to play.\n")
            print("""Here is a list of current supported games:
            a: Cataclysm: Dark Days Ahead,
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
                    os.system("wget https://github.com/DGoldDragon28/Unangband/releases/download/v.0.6.6/unangband-066-linux.tgz")
                    os.system("tar -xzvf unangband-066-linux.tgz")
                    os.system("cd unangband-066-linux")
                    os.system("chmod +x unangband")
                elif element == "d":
                    os.system("echo 'deb https://crawl.develz.org/debian crawl 0.26' | sudo tee -a /etc/apt/sources.list")
                    os.system("wget https://crawl.develz.org/debian/pubkey -O - | sudo apt-key add -")
                    os.system("sudo apt-get update")
                    os.system("sudo apt-get install crawl")
                else:
                    pass
                


init()
    