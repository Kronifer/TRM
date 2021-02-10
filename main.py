#! /usr/bin/python3.7

import kvJSON as kv
import os

def init():
    kv.init("data.json")
    try:
        kv.getData("gamelist")
    except:
        config = input("It seems you have not configured TRM yet. Would you like to now? If no, TRM will be autoconfigured. [y/n] ")
        if config == "y":
            os.system("clear")
            print("First, you need to decide what games you want users to play.")

