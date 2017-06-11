#!/usr/bin/python

import shutil
import os
import argparse
import subprocess

if not shutil.which("xrandr"):
    print("Xrandr not found. Please install xrandr and try agian")
    exit(1)

if not os.getuid() == 0:
    print("Please run as administrator")
    exit(1)

parser = argparse.ArgumentParser(description='Generates custom resolutions for better HiDPI support')
parser.add_argument("horizontal", help="horizontal resolution", metavar="H", type=int, nargs=1)
parser.add_argument("vertical", help="vertical resolution", metavar="V", type=int, nargs=1)
parser.add_argument("output", help="output display", metavar="Out", nargs=1)
parser.add_argument("--apply", "-a", help="set resolution after creation", action='store_true')
parser.add_argument("--save", "-s", help="save resolution to desktop file (for use as a startup application)", action='store_true')

args = parser.parse_args()

cvt_stdout = subprocess.run(['cvt', str(args.horizontal[0]*2), str(args.vertical[0]*2), "60"], stdout=subprocess.PIPE).stdout.decode("utf-8")
cvt = " ".join(cvt_stdout.split("\n")[1].split(" ")[1:])

subprocess.run(['xrandr', "--newmode", str(cvt)])
subprocess.run(['xrandr', "--addmode", args.output[0], str(args.horizontal[0]*2)+"x"+str(args.vertical[0]*2)+"_60.00"])
subprocess.run(['xrandr', "-s", str(args.horizontal[0]*2)+"x"+str(args.vertical[0]*2)])
