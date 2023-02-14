#!/usr/bin/python3

import os
import sys

ip = input("Enter 127.0.0.1: ")
port = input("Enter 4444: ")

for filename in os.listdir("."):
    if filename.endswith(".py"):
        with open(filename, "r") as f:
            filedata = f.read()

        filedata = filedata.replace("127.0.0.1", ip)
        filedata = filedata.replace("4444", port)

        with open(filename, "w") as f:
            f.write(filedata)
