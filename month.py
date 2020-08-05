from bs4 import BeautifulSoup
import re

url = "/home/alessandro/Scrivania/Repos/Football-Counter-Bot/messages.html"


def getTexts(source):
    page = open(source)
    soup = BeautifulSoup(page.read(),features='lxml')
    divs = soup.findAll('div', {'class':'text'},text=False)
    filteredText = []

    for div in divs:
        content = div.text

        for i in  range(0,len(content)-1):
            if i < len(content)-1:
                if content[i].isdigit() and not content[i+1].isdigit():
                    filteredText.append('\n')
            
            filteredText.append(content[i+1])

    return ''.join(filteredText).lstrip()

def removeWhiteSpace(word):
    newWord = []
    text = word.splitlines()

    for t in text:
        newWord.append(t.lstrip() + '\n')
    
    return ''.join(newWord).lstrip()
        

def toDictList(words):
    dictList = list()

    for word in words:
        if word is not '':
            data = word.split(' ')

            if (len(data) == 2  and len(data[1]) > 0):
                elem = {
                    'word':data[0],
                    'count':int(data[1])
                }
                dictList.append(elem)
    
    return dictList


def countDictList(elements):
    newDictList = list()

    for elem in elements:
        found = False
        for newDictElement in newDictList:
            if (elem['word']  == newDictElement['word']):
                newDictElement['count'] += elem['count']
                found = True
        if not found:
            newDictElem = {
                'word':elem['word'],
                'count':elem['count']
            }
            newDictList.append(newDictElem)
    
    return newDictList

def printDictList(dictList):
    for elem in dictList:
        print(elem['word'] + ' ' + str(elem['count']) + '\n')

            
        
words = removeWhiteSpace(getTexts(url)).splitlines()

elements = toDictList(words)

filteredElements = countDictList(elements)

orderedElements = sorted(filteredElements, key=lambda k: k['count'])

printDictList(orderedElements)
