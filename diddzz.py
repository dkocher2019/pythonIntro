# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 18:39:59 2019

@author: Dan
"""

#########################################################################################
######  Welcome to your new and awesome python tutorial: ft. random linux commands ######
#########################################################################################       

## PS: Scroll down past methods for main. You can try putting it above. but. Well. The way this file is parsed
## says thats a no-no        


########################
###      Imports     ###
########################

#This is a python library easy to import, generally when you google weird functions youll need to add one of these
import csv    

#This is from the sibling file to what i sent, we import the command class constructor from it. Needs to be in same directory or specified in some other way
from Command import Command
    
def loopDemo(dumb_variable):
    """
    This is a docString. Pythons random way of giving a coder a nice way to format method descriptions
    Rules are simple, first word should be capitalized, and you know... basic grammar stuff should follow.
    It's worth noting that most people expect this section to describe what a method does, and NOT HOW. 
    This is kind of like the pirate code... more of a guideline. 
    *Note, be very careful with indents on these Python is picky
    
    --This method demonstrates basic looping structures and syntax. Not all, but some that I've found useful.
    :Param dumb_variable: an otherwise useless variable that was not loved as a child
    """
    dumb_variable = 6  #Side note: This will not change the variable outside of this scope. You know this. I hope you know this.
    
    
    #Alright, loops. So python has a lot of ways to loop through things and is pretty generous
    #Lets say you have a list
    
    useful_commands = ["cd", "mkdir", "rm", "ls", "mv", "man", "touch"]
    
    # Cool. Now how many ways can we loop through this?
    
    #############################
    #####    Normal Loop    #####
    #############################
    for x in useful_commands:
        print(x)
    print() ## just for spacing
    #############################
    #####    Range Loop     #####
    #############################
    for x in range(0,7):
        print(useful_commands[x])
    else:
        print("This else will happen at the end of the loop. Optional\n")
        
    #############################
    #####    While Loop     #####
    #############################
    x = -7
    while x < 0:
        print(useful_commands[x])
        x+=1
    print()
    
    #############################
    #####  Dumb While loop  #####
    #############################
    # HW QUESTION (EASY) why doesn't cd print? ... I honestly just didnt feel like changing stuff...
    x+=1    
    while x:
        print(useful_commands[x])   
        x+=1
        if x is 7:
            break
        if x == 7:
            break
    print()
    #############################
    #####    Do-While loop  #####
    #############################
    dedicated = False
    
    if dedicated: 
        print("Haha... good one, look it up yourself if you really want it.")
    
    #But wait 先生, doesn't this function not return anything?
    #True... but python doesn't care
    return 7

def objectDemo(printSimple, printDef):
    """
    A simple Demo of how to create objects and instantiate them. Also has some
    bonus file I/o stuff for giggles because why not. 
    :param printSimple: boolean flag for type of output
    :param printDef: boolean flag... blah 
    """
    
    #Below is how you create a list object. It starts empty, is sorted and mutable (can be appended to)

    ## Real quick tangent. Sets, are unordered, cannot contain duplicates, and are mutable. So choosing between
    ## the two can occasionaly make a difference. 
    commandObjectList = []
    
    #Couple things to note below
    ## 1.) open, takes the file name (with extension) and a character that represent file permissions. in this case 'r' specifies read only. 'w' is write only
    ## 2.) as <"x"> just means that we are aliasing the file pointer to "x". So anytime we want to access that file, we use x, not the filename or whatever. 
    ## 3.) a csv file is just a comma seperated (value) file. (Excel lets you save them like this)
    ## 4.) csv.reader references the imported library. Reader is a method provided and allows for easy iteration through the csv
    with open("LinuxCMDS.csv",'r') as csvfile:
        cmdReader = csv.reader(csvfile)
        next(cmdReader, None)            # skip the header
        for row in cmdReader:
            #Below is how you call the command constructor in the other file, notice the lack of the self param.
            commandObj = Command(row[0], row[1], row[2], row[3])
            commandObjectList.append(commandObj)
        
    if printSimple:
        print("|   Command     |    English'd     |  Coolness  |")
        print("|_______________|__________________|____________|")
        # IM being lazy, there are better ways to do tables
        for obj in commandObjectList:
            #printCommand is a method specific to the command class and must be referenced with an object (a non static java method)
            obj.printCommand()
            
    if printDef:
        print("|Command| Definition:")
        for obj in commandObjectList:
            obj.printDefinition()
        print("****NOTE**** cd . and cd .. can be used to display the current directory and move to the previous directory respectively")
    
    

if __name__ == '__main__':
    # Here's some flags that I set to demonstrate some features
    #  * NOTICE: no types required because python is your friend  ... ... .................................. except when its not
    runLoopDemo = True
    runObjectDemo = True
    
        
    ##Some secondary flags for how you want stuff printed
    
    ## *NOTE* formating gets wonky depending on size of terminal (you can click and drag it to make bigger) I was also a little bit lazy with formatting... a teensy bit
    printDefinitions = True
    printSimple = True
    
    
    
    #Here's a ...
    useless_variable = (6, "CD is how you change directories")
    #I'm going to pass this as a parameter, and notice it doesn't care about type specification
    #(it's type is technically a tuple2 (a tuple3 would be like (1,"apple",5) the individual parts
    # don't matter, just that there is the right number of them))
    if runLoopDemo:
        #Definied at the top of the file
        loopDemo(useless_variable)
        
    if runObjectDemo:
        #defined below loopDemo
        objectDemo(printSimple,printDefinitions)
        
#    if runFormatDemo:
#        formatDemo()
        