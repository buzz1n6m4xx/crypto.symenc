#!/usr/bin/env python

"""This program shows an example of symmetric encryption.
You can either generate a key file (randomized mapping list, based on an input file) or use an existing key file to encode/decode strings of previous sessions.
The default input file is based on the standard ASCII (printable characters) table (character code 32-126), and extended by some specific ASCII codes. The full ASCII code table can be reviewed for example at https://www.ascii-code.com/
"""

__author__ = "buzz1n6m4xx"
__status__ = "Production"
__version__ = "0.1"

from numpy import random, savetxt
from sys import exit
from os import getcwd

### VARIABLES ###    
    
charstr = "\nYour entered text: "
encstr = " has been encoded to:\n\n"
decstr = " has been decoded to:\n\n"

indxstr = " with index number "
matchstr = " has been re-assigned to index number "
encryptstr = " respectively character "

txtcolreset = "\x1b[0;0m"
txtcolgr = "\x1b[1;32m"
txtcolbd = "\x1b[1m"

charset = []
match = []
keyset = []                                                         # list for input file content
idxset = []                                                         # temp list to save indices of normal text characters
eidxset = []                                                        # temp list to save indices of encoded text characters
  
### OPEN AND SAVE INPUT FILE ###

inputfile = open('ascii.csv','r')                                   # open input file in read-only mode
prepfile = inputfile.read().splitlines()                            # remove line breaks from each line

for row in prepfile:                                                # append input file content to list (line by line)
    charset.append(row)                                             # store character in list

inputfile.close()                                                   # close input file

### FUNCTIONS ###
                                    
### GENERATE KEY ###

def generateKey(charset):                                           # define function random item selector for list
    
    chars = len(charset)                                            # count items in list
    
    return random.choice(charset, chars, False)                     # return unique item for all list items (from numpy)
    
def encode(inputtext, match, idxset):
                                                
    text = list(inputtext)                                          # converts input string to list

    for idx in text:                                                # each item in input list
        index_textfile = charset.index(idx)                         # get index number of item from input file list
        enc = (match[index_textfile])                               # use according index number of key list (match)
        idxset.append(enc)                                          # store character to list
        encodedtext = ''.join([str(item) for item in idxset])       # convert each elememt in list (int and/or strg) to a string, and create a new string list
    
    print(txtcolreset + charstr + txtcolgr + inputtext + txtcolreset + encstr + encodedtext)

### DECODE FUNCTION ###

def decode(inputenc, match, eidxset):
   
    enctext = list(inputenc)

    for eidx in enctext:
        index_keyfile = match.index(eidx)
        dec = (charset[index_keyfile])
        eidxset.append(dec)
        decodedtext = ''.join([str(item) for item in eidxset])
              
    print(txtcolreset + charstr + txtcolgr + inputenc + txtcolreset + decstr + decodedtext) 

### USER INPUT MENU FUNCTION ###

def callOption(option):

    while option not in {"1", "2", "3", "4"}:                       # allow only valid options
        option = None
        option = input("\nPlease enter an option 1, 2, 3 or 4: ")
    
    while option == "1":
        idxset = []                                                 # list needs to be cleared before passing to the encode function
        eidxset = []                                                # list needs to be cleared before passing to the decode function
        key = generateKey(charset)                                  # generates key / saves randomized output to array
        match = key.tolist()                                        # converts array to list
        savetxt("key.csv", key, delimiter=" ", fmt="%s")            # exports list to file (from numpy)
        directory = getcwd()                                        # get current working directory (import os)
        
        inputtext = input(txtcolgr + "\nEnter some text to encode: ")
        encode(inputtext, match, idxset);                           # call encode function and pass parameters
        
        inputenc = input(txtcolgr + "Now copy/paste/modify the encoded string to decode again: ")
        decode(inputenc, match, eidxset);                           # call decode function and pass parameters
        
        print(txtcolreset + "\n\nYour encryption key has been saved to \"" + directory + "\\key.csv\" \nIf you quit at this stage the saved \"key.csv\" needs to be imported to be reused again.")
        input(txtcolgr + "To continue to options, press Enter: ")
        
        init();                                                     # call start function
        
    while option == "2":
        idxset = []                                                 # list needs to be cleared before passing to the function
        inputkeyfile = open('key.csv','r')                          # use existing key.csv file as key file
        prepkeyfile = inputkeyfile.read().splitlines()              # remove line breaks from each line
            
        for row in prepkeyfile:                                     # append key file content to list (line by line)
                keyset.append(row)                                  # store character in list
                
        inputkeyfile.close()                                        # close key file
        match = keyset
        
        inputtext = input(txtcolgr + "\nEnter some text to encode: ")
        encode(inputtext, match, idxset);                           # call encode function and pass parameters
        
        input(txtcolgr + "To continue to options, press Enter: ")
        init();                                                     # call start function
        
    while option == "3":
        eidxset = []                                                # list needs to be cleared before passing to the function
        inputkeyfile = open('key.csv','r')                          # use existing key.csv file as key file
        prepkeyfile = inputkeyfile.read().splitlines()              # remove line breaks from each line
            
        for row in prepkeyfile:                                     # append input file content to list (line by line)
            keyset.append(row)                                      # store character in list
                                      
        inputkeyfile.close()                                        # close key file
        match = keyset
        
        inputenc = input(txtcolgr + "Paste some encoded text to decode: ")
        decode(inputenc, match, eidxset);                           # call decode function and pass parameters
        
        input(txtcolgr + "To continue to options, press Enter: ")
        init();                                                     # call start function
        
    if option == "4":
        print(txtcolreset + "\nBye")
        exit()                                                      # quit program(from sys)

### INIT/START FUNCTION ###

def init():

    print(txtcolreset)
    print(txtcolbd + "\n\nUnderstanding Symmetric Encryption")
    print("**********************************")
    print(txtcolreset + "\nThis program shows an example of symmetric encryption.")
    print("\nYou can either generate a key file (randomized mapping list, based on an input file) or use an existing key file to encode/decode strings of previous sessions.")
    print("\nThe default input file is based on the standard ASCII (printable characters) table (character code 32-126), and extended by some specific ASCII codes. The full ASCII code table can be reviewed for example at https://www.ascii-code.com/")
    print(txtcolgr + "\nSelect an option to continue: " + txtcolreset)
    print("\n (1) Generate a new key file to encode/decode data")
    print(" (2) Use an existing key file to encode data")
    print(" (3) Use an existing key file to decode data")
    print(" (4) Quit program")

    option = input(txtcolgr +"\n (1/2/3/4) : ")
    
    callOption(option);                                             # call user input menu function

### START PROGRAM ###
    
init();                                                             # call start function                     