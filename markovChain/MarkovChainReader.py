#This script is used to generate text based on a NGramsList.txt file.
# Use MarkovChainParser.py to generate the document from natural language.


from random import random
from random import seed
import sys

ngrams = []


class NGram:
    text = ""
    nextN = [] #Index of possible next words
    nextNCount = [] #Number of each next word that has been added


    def __init__(self, text):
        self.text = text
        self.nextN = []
        self.nextNCount = []

    def GetNextRandomIndex(self):
        probs = []
        if len(self.nextNCount) > 0:
            for c in self.nextNCount:
                probs.append(float(c) * random())
            return int(self.nextN[ probs.index(max(probs)) ])

#================================================================================================
        
def ReadNGramsFromFile(inPath):
    fIn = open(inPath, "r", encoding="utf8")

    lines = fIn.read().split()


    ngrams = []

    for l in lines:
        ParseLineAsNGram(l)


def ParseLineAsNGram(line):
    parts = line.split("#")
    ngram = NGram(parts[0])
    del parts[0]
    for p in parts:
        part = p.split("|")
        if len(part) > 1:
            ngram.nextN.append(part[0])
            ngram.nextNCount.append(part[1])
        else:
            ngram.nextN.append(1)
            ngram.nextNCount.append(1)
        
    ngrams.append(ngram)

#Capitalizes the first letter of each sentence, determined by the delimiter
def CapitalizeBySentence(sentences, delim):
    s = sentences.split(delim)
    for i in range(len(s)):
        firstLetter = (s[i])[0].capitalize()
        s[i] = firstLetter + (s[i])[1:]
        
    return delim.join(s)

def CapitalizePronouns(sentences):
    return sentences.replace(' i ', ' I ').replace('i.', 'I.').replace(" i'", " I'")
    
def GenerateSentence(startIndex, maxWords):
    s = ""
    
    indexPointer = startIndex
    for i in range(maxWords):
        s += ngrams[indexPointer].text + " "
        indexPointer = ngrams[indexPointer].GetNextRandomIndex()


#Properly capitalize the sentences
    for punc in ['. ', '! ', '? ']:
        s = CapitalizeBySentence(s, punc)

    s = CapitalizePronouns(s)
    
    print(s)

#==========| START |==========


sd = ""
length = 10


#===| INPUT |===
sd = input("Enter a random seed: ")
length = int(input("How many words to output: "))

seed(sd)

ReadNGramsFromFile("./NGramsList.txt")

# for n in ngrams:
#    print(n.text + "\n" + str(n.nextN) + "\n" + str(n.nextNCount))

GenerateSentence(int(random() * (len(ngrams) - 1)), length)