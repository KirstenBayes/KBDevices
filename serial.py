## How to Convert Data coming in via a Serial Port into Python lists for analysis

## Props to Paul McWhorter (toptechboy.com) for teaching me how to do this (without error checking) for Arduinos. All mistakes are mine, though!
## Need to load and debug with an actual microbit when it becomes available: use with caution
## Pay particular attention to the white space (indenting, blank lines), which matters in Python

## Use the pyserial library to talk to the serial port, or USB: the import name for this is 'serial'

import serial 

## Use the numpy library, a very commonly used math library from Python

import numpy  

## set up a Serial port object that reads data coming off the micro:bit - note the baud rate must be the same as the micro:bit,
## you will also need to find the com port yourself (sorry!): will vary from Windows to Python to Mac.

microbitData = serial.Serial('com11', 115200)

## Create the tempC and pressurePa lists (list type), which will take the data coming off the serial port from two example sensors

tempC = []
pressurePa = []


## The following presumes you have data coming off the microbit device in strings: value pairs delimited by a comma and ended with an end of line (EOL).
 
     
while True: 
    while (microbitData.inWaiting()==0):     #Wait here until there is data
        pass                                 #While we wait, do nothing
    microbitString = microbitData.readline() #read the line of text from the serial port object microbitData, and put it into the microbitString variable
    dataArray = microbitString.split(',')    #Split microbitString into an array called dataArray, and make the split on a comma delimiter 
    temp = float(dataArray[0])               #Convert first element (count from zero) to floating number and put in temp         
    p = float(dataArray[1])                  ## Convert second element to floating number and put in p                 
    tempC.append(temp)                       #Build our tempC list by appending temp readings
    pressurePa.append(P)                     #Building our pressurePa list by appending P readings
    




     
## Once you have the connection working, see what errors the device is throwing: trap the errors using code like the following

try:
    temp = float(dataArray[0])
except ValueError:
    temp = np.NaN
else:
    temp = float(dataArray[0])


