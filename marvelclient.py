#!/usr/bin/env python3
# nameclient.py - Program to receive web name lookup command
# This CGI program used the python nameserver to lookup names
# And retuen result to web page
# James Skon, 2019
#!/usr/bin/env python
import os
from os import path
import sys

import cgi;
import cgitb
cgitb.enable()

fifoname="harrington1"  # Unique name for fifos
commandFifoFile = "/tmp/"+fifoname+"_commandFifo"
resultFifoFile = "/tmp/"+fifoname+"_resultFifo"
def print_header():
    print ("""Content-type: text/html\n""")

def callMarvelServer(name):
    #Create Fifos if they don't exist
    if not path.exists(commandFifoFile):
        os.mkfifo(commandFifoFile)
    if not path.exists(resultFifoFile):
        os.mkfifo(resultFifoFile)

    commandFifo=open(commandFifoFile, "w")
    resultFifo=open(resultFifoFile, "r")
    commandFifo.write(name)
    commandFifo.close()

    result=""
    for line in resultFifo:
        result+=line
    resultFifo.close()
    return(result)

def main():
    form = cgi.FieldStorage()
    if (form.getvalue("name")):
        print_header()
        name=form.getvalue("name").lower()
        result=callMarvelServer(name)
        # Send back to webpage
        print(result)
    else:
        print("Error in submission")
        
main()
