#!/usr/bin/python3

import os
import sys

def replace_in_files(directory, target_ip, target_port):
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                contents = file.readlines()

            with open(filepath, "w") as file:
                for line in contents:
                    if "sock.connect" in line or "s.connect" in line:
                        line = line.replace("'IP'", f"'{target_ip}'")
                    if "), PORT)" in line:
                        line = line.replace(", PORT)", f", {target_port})")
                    file.write(line)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Please provide target IP and PORT as arguments")
        sys.exit()
    
    target_ip = sys.argv[1]
    target_port = sys.argv[2]
    replace_in_files(".", target_ip, target_port)
