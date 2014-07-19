"""Here are your instructions:
Make a FileHandling_Homework project and assign it to your Python2_Homework working set. In that project, write a module containing a function to examine the contents of the current working directory and print out a count of how many files have each extension (".txt", ".doc", etc.)

Write a separate module to verify by testing that the function gives correct results."""
 
############################################################################################################################################################################################################################################################################################################################

import os
import glob

def filecount(dir):
    result={}
    os.chdir(dir)
    b = glob.glob("*.*")
    
    for things in b:
        c = things.rfind('.')
        type_variable = things[c+1:]
        if type_variable not in result:
            result[type_variable]=1
        else:
            result[type_variable] += 1
        if "subdir" in type_variable:
            del result[type_variable]
            
    
    return (result)
    

if __name__=="__main__":
    a=os.getcwd()
    for files in filecount(a):
        print(files,filecount(a)[files])



 
 
