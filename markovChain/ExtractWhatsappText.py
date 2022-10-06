# A simple script to nicely format a downloaded whatsapp chat file, such that
# it may be used as input to feed the Markov generator

# NOTE: Input file MUST be named "Paragraph.txt"

fIn = open("Paragraph.txt", "r", encoding="utf8")

lines = fIn.readlines()

fIn.close()

wantedlines = []

for l in lines:
    if l[-2] in [c for c in "abcdefghijklmnopqrstuvwxyz"]:
        #print(l[-2])
        wantedlines.append(l[:-1] + ".\n")


fOut = open("Paragraph2.txt", "w+", encoding="utf8")

for l in wantedlines:
    fOut.write(l)


fOut.close()