"""Here are your instructions:

Write a function (not a class) that takes two arguments, a string player name and an integer score,
and keeps a "high score" table in a Python shelve. If the integer argument is higher than the given player's
current high score (or if the player has no recorded high score), log the value as this player's new high score. 
The function should return the player's current high score. Remember, a function is not the same thing as a class
and it's a function that's needed.

Again, write a separate test module that verifies the operation of the function."""
 
#############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

import shelve
import os

def Scores(name,score):
    os.chdir('.')
    shelf = shelve.open(r'myshelf.shlf')
    
    if name not in shelf.keys():
        shelf[name] = score
        
        
    elif name in shelf.keys(): 
        if score > shelf[name]:    
            shelf[name] = score
    
    hs=shelf[name]    
    shelf.close()
    return hs

