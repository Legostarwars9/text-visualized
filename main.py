#!/usr/bin/env python3
import os
import sys
import read
import time
import write
import GUI
from pathlib import Path
#Default Variables
version = "0.0.1a"
output = Path.cwd() / "output.png"
cwd = Path.cwd()
verbose = False
x = 10
y = 10
#Def Funcs
def pgm_help(synerr):
    if synerr == 1:
        print("")
        print("! Syntax Error !")
    print("""
Usage:
    txt2img <input_file> [options]

Options:
    -h --help           Show this help page
    -v --verbose        Show more information (Live Logging)
    -V --version      Show version
    -o --output <file>  Specify output file
    -r --read           Read Image
    -g --gui            Start in GUI
How 2 Use:
    txt2img makes a image with color data based on the input .txt file or allows the reverse with the -r flag
    using the -r flag requires you to input an image and it will output a .txt file based on the data in the image
    Only PNGs are supported.
    """)
    sys.exit()

#Program
if "-g" in sys.argv or "--gui" in sys.argv:
    GUI.startgui(x,y)
    sys.exit(0)

if "-h" in sys.argv or "--help" in sys.argv:
    pgm_help(0)
    sys.exit(0)

if "-V" in sys.argv or "--version" in sys.argv:
    print("Version:",version)
    sys.exit(0)

if "-v" in sys.argv or "--verbose" in sys.argv:
    verbose = True

if sys.argv[1].startswith("-"):
    pgm_help(1)
    sys.exit(1)

if not sys.argv[1].endswith((".png", ".txt")):
    print("Invalid file type")
    sys.exit(0)

if "-o" in sys.argv or "--output" in sys.argv:
    output = sys.argv[sys.argv.index("-o") + 1]
    output = output + "/output.png"
    print("Custom Output:",output)

if "-r" in sys.argv or "--read" in sys.argv:
    if sys.argv[1].startswith(("/", "~")) and sys.argv[1].endswith(".png"):
        read.read(sys.argv[1])
    if not sys.argv[1].startswith(("/", "~")) and sys.argv[1].endswith(".png"):
        if Path.exists(Path(sys.argv[1]).resolve()) and verbose == True:
            print("File Path:", Path(sys.argv[1]).resolve())
            time.sleep(0.5)
        else:
            time.sleep(0.5)
        if Path.exists(Path(sys.argv[1]).resolve()):
            read.read(Path(sys.argv[1]).resolve(), verbose)
        else:
            print("File not found")
            sys.exit(0)

if sys.argv[1].startswith(("/", "~")) and sys.argv[1].endswith(".txt"):
    write.write(sys.argv[1])
if not sys.argv[1].startswith(("/", "~")) and sys.argv[1].endswith(".txt"):
    if Path.exists(Path(sys.argv[1]).resolve()) and verbose == True:
        print("File Path:", Path(sys.argv[1]).resolve())
        time.sleep(0.5)
    else:
        time.sleep(0.5)
    if Path.exists(Path(sys.argv[1]).resolve()):
        write.write(Path(sys.argv[1]).resolve())
    else:
        print("File not found")
        sys.exit(0)