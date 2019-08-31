# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:33:03 2019

@author: Dan
"""

class Command(object):
    
     def __init__(self, cmdName, meaning, definition, coolnessLevel):
         """
         This is a constructor for the given class. Can be used to instantiate an object with specific
         parameters. Self does not need to be specified when this is being called, it is automatically included.
         :param cmdName: string representing the name of a keyword to be used on the linux command line
         :param meaning: cmdName but with more letters
         :param defintion: How Webster defines the function of cmdName
         :param coolnessLevel:  important value that specifies how cool you are for using a specific command
         (really just how useful I've found the command)
         -Basic constructor to be used to make command objects for storage in a dictionary and printed for reference
         """
         
         # the Self operator is like the "this" operator in java, just specifies that we are assigning the right hand
         # side to the specific instance variable of the CURRENT object
         self.cmdName = cmdName
         self.meaning = meaning
         self.definition= definition
         self.coolnessLevel = int(coolnessLevel)   ## Disclaimer, sooo... I mightve mentioned no type casting... well... this is for formatting... an exception that i forgot about... there are a few... i forget stuff.... deal with it.
    
     def printCommand(self):
        print("|%15s|%18s|%12d|" %(self.cmdName, self.meaning, self.coolnessLevel))
        
     def printDefinition(self):
        print("|%7s|%-60s" %(self.cmdName, self.definition))
       
        