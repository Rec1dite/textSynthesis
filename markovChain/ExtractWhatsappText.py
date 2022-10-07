# A simple script to nicely format a downloaded whatsapp chat file, such that
# it may be used as input to feed the Markov generator

import os

inFile = ""
while inFile == "":
    inFile = input("Enter the name of the exported Whatsapp chat file to parse: ")
    if not os.path.exists(inFile):
        inFile = ""
        print("File does not exist!")

fIn = open(inFile, "r", encoding="utf8")

lines = fIn.readlines()

fIn.close()

wantedlines = []

for l in lines:
    if l[-2] in [c for c in "abcdefghijklmnopqrstuvwxyz"]:
        #print(l[-2])
        wantedlines.append(l[:-1] + ".\n")


[inFileName, inFileExt] = inFile.rsplit('.', 1)
fOut = open(inFileName + "_parsed." + inFileExt, "w+", encoding="utf8")

for l in wantedlines:
    fOut.write(l)


fOut.close()