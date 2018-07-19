#!/usr/local/bin/python3

import sys
import serial
from time import sleep

port = sys.argv[1]
blastfilename = sys.argv[2]

print('Using serial port: {port}')

ser = serial.Serial(port, 115200, timeout=1)

def writeFile(filename, ser):
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        ser.write(bytes(line.strip(), 'cp437'))
        ser.write(bytes('\n', 'cp437'))
        sleep(0.05)
    f.close()

while(True):
    writeFile(blastfilename, ser)
    sleep(0.05)


