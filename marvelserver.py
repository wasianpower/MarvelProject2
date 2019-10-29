import os 
from os import path 
import sys

#Git lab test comment
#from sortedcontainers import SortedDict
#filePath="/home/class/SoftDev/namedata/"

def readfile(filename):
  infile=open(filename,mode='r')
  array=[]
  for line in infile:
    templine=line
    array.append(templine.split(','))
  infile.close()
  return array[::-1]

def removePunctuation(s):
  #Remove all punctuation from a string
  import string
  for c in string.punctuation:
    s= s.replace(c,"")
  return s

def createNameIndex(array):
  #creates an index of every name and the number of the lines that have that number on it
  index={}
  arraylen=len(array)
  for x in range(arraylen):
    allnames=removePunctuation(array[x][1]).lower().split(' ')
    #catalogs each name, so "Peter Parker" will also appear when you search for just Peter or Parker. This has an added benefit in that it allows the program to determine answers more relevant to the search, see the sortrelevancy function
    for name in allnames:
      if not name in index:
        index[name]=[x]
      else:
        index[name].append(x)
  return index

def createYearIndex(array):
  #creates an index the same as the name index, except with years instead of names
  index={}
  arraylen=len(array)
  for x in range(arraylen):
    year=array[x][12][0:4]
    if year in index:
      index[year].append(x)
    else:
      index[year]=[x]
  return index

#def display(infolist):
#  #displays all the information in a way that's easy to read
#  print(infolist[1].replace("\"",'').replace("\\",''))
#  print()
#  print("First Appearance: "+infolist[11][0:3]+" "+infolist[12])
#  print("Total Appearances: "+infolist[10])
#  print("Alignment: "+infolist[4].replace("Characters",''))
#  print("Status: "+infolist[9].replace("Characters",''))
#  print("Identity: "+infolist[3].replace("Identity",''))
#  print("Gender: "+infolist[7].replace("Characters",''))
#  print("Eyes: "+infolist[5].replace("Eyes",''))
#  print("Hair: "+infolist[6].replace("Hair",''))
  

def searchFor(term,nameindex,yearindex):
  #searches the indexes for the desired term, keeping track of each row that comes  back, including duplicates, which will be used by sortRelevancy
  allterms=term.split()
  allterms.append(term)
  allterms.append(term.replace(" ",''))
  results=[]
  for word in allterms:
    if word in nameindex:
      for number in nameindex[word]:
        results.append(number)
    if word in yearindex:
      for number in yearindex[word]:
        results.append(number)
  return results


def print_header():
    print ("""Content-type: text/html\n""")

def sortRelevancy(numberlist):
  #counts the number of times that each answer has appeared, then sorts them in that order so that the name that appeared the most times is at the top.
  sortednumbers={}
  for number in numberlist:
    if not number in sortednumbers:
      sortednumbers[number]=1
    else:
      sortednumbers[number]=sortednumbers[number]+1
  finallist=sorted(sortednumbers.items(), key=lambda kv:(kv[1], kv[0]))
  finallist= finallist[::-1]
  return finallist[0:10] # to prevent too many results, only the 10 most relevant are shown


def nameServer():
  fifoname="harrington1" # unique name for fifos
  commandFifoFile = "/tmp/"+fifoname+"_commandFifo"
  resultFifoFile = "/tmp/"+fifoname+"_resultFifo"

  #Create Fifos is they don't exist
  if not path.exists(commandFifoFile):
    os.mkfifo(commandFifoFile)
  if not path.exists(resultFifoFile):
    os.mkfifo(resultFifoFile)

  print("Building namemaps ...",end="")
  filename=readfile('/home/class/SoftDev/marvel/marvel-wikia-data.csv')
  marvelindex=createNameIndex(filename)
  yearindex=createYearIndex(filename)
  print("done!");
  
  # Main loop.  Wait for message, process it, and return result.  Then loop.
  while True:
    print("Wating for command");
    commandFifo=open(commandFifoFile, "r")
    resultFifo=open(resultFifoFile, "w")

    line = commandFifo.read()
    print("Command Recieved: ",line)
    name=line

    resultlist=sortRelevancy(searchFor(name,marvelindex,yearindex))
    result=" " #str(len(resultlist))
    for heroes in resultlist:
      if len(result) > 0:
        result+=filename[heroes[0]][1] + "," + "https://marvel.fandom.com/wiki" + filename[heroes[0]][2][1::] + ', ' + filename[heroes[0]][11][0:3] + " " + filename[heroes[0]][12] + ", " + filename[heroes[0]][10] + ", " + filename[heroes[0]][4].replace("Characters",'') + ', ' + filename[heroes[0]][9].replace("Characters",'') + ', ' + filename[heroes[0]][3].replace("Identity",'') + ', ' + filename[heroes[0]][7].replace("Characters",'') + ', ' + filename[heroes[0]][5].replace('Eyes','') + ', ' + filename[heroes[0]][6].replace("Hair",'') + ', '
      
    print("Sending:",result)

    resultFifo.write(result)
      
    resultFifo.close()
    commandFifo.close()


nameServer()
