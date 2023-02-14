#!/usr/bin/python3

import os
import sys

ip = input("Enter IP: ")
port = input("Enter PORT: ")

for filename in os.listdir("."):
    if filename.endswith(".py"):
        with open(filename, "r") as f:
            filedata = f.read()

        filedata = filedata.replace("IP", ip)
        filedata = filedata.replace("PORT", port)

        with open(filename, "w") as f:
            f.write(filedata)
