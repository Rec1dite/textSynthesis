#Parses a natural language text file into a NGramsList.txt file.

import os

ngrams = []

#Holds a single word, along with the next possible words that may follow it
class NGram:
    text = ""
    nextN = [] #Index of possible next words
    nextNCount = [] #Number of each next word that has been added


    def __init__(self, text):
        self.text = text
        self.nextN = []         #NOTE: Needed to initialise the value as empty, else it is assumed to be static, and all NGrams will have the same nextN value
        self.nextNCount = []


    #Add new nextN entry; handles duplicates
    def newNextWord(self, nextWordIndex):
        if nextWordIndex != -1:
            
            added = False
            #Check if next words already exists
            for i in range(len(self.nextN)):
                if self.nextN[i] == nextWordIndex:
                    self.nextNCount[i] += 1
                    added = True
        
            if not added:
                self.nextN.append(nextWordIndex)
                self.nextNCount.append(1)


#================================================================================================

#Adds a new NGram to the list; prevents duplicates
def addNewNGramWithoutNextWord(text):   #Only creates the ngrams, doesn't fill them with values yet
    created = False
    for n in ngrams:
        if n.text == text:
            created = True


    #Create new NGram
    if not created:
        n = NGram(text)
        ngrams.append(n)



def addNewReference(text, nextWordIndex):   #Only creates the ngrams, doesn't fill them with values yet
    for n in ngrams:
        if n.text == text:
            n.newNextWord(nextWordIndex)
            break
            

#Returns the index of the ngram matching the specified string
def GetNGramIndex(text):
    for n in range(len(ngrams)):
        if ngrams[n].text == text:
            return n
        
    return -1


#Reads from a paragraph file and converts it into a list of ngrams
def ParseParagraph(paraPath):
    fIn = open(paraPath, "r", encoding="utf8")
    words = fIn.read().split()
    fIn.close()

    ngrams = []

    #Fill ngrams with words, but without next word references
    for w in words:
        addNewNGramWithoutNextWord(w)


    #Create next word references between the ngrams
    for i in range(len(words)):
        nextIndex = 0
        if i < len(words)-1:
            nextIndex = GetNGramIndex(words[i + 1])
        else:
            nextIndex = -1
            
        addNewReference(words[i], nextIndex) #A value of -1 signifies and empty word, and will not be added to the nextN nor the nextNCount list


#Writes the current ngrams to a file [Destroys current file data]
def WriteNGramsToFile(outFile):
    fOut = open(outFile, "w", encoding="utf8")

    for n in ngrams:
        s = ""
        for nxt in range(len(n.nextN)):
            s += str(n.nextN[nxt]) + "|" + str(n.nextNCount[nxt]) + "#"

        s = s.rstrip('#')
        
        fOut.write(n.text + "#" + s + "\n")

    fOut.close()



#==========| START |==========

inFile = ""
while inFile == "":
    inFile = input("Enter the name of the input text file: ")
    if not os.path.exists(inFile):
        inFile = ""
        print("File does not exist!")

ParseParagraph(inFile)

WriteNGramsToFile("./NGramsList.txt")

i = 0
for n in ngrams:
    print("[" + str(i) + "] " + n.text + "\n" + str(n.nextN) + "\n" + str(n.nextNCount) + "\n")
    i += 1