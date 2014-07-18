Here are your instructions:

The zipfile example in the lesson text stores the full path of the files that it saves to the zipfile. Normally, however, zipfiles contain only a relative pathname (you will see that when the names are listed after the zipfile is created, the "v:\\" has been removed).

Create a project named Archives_Homework and add it to the Python2_Homework working set. In this project, write a function that takes a directory path and creates an archive of the directory only. For example, if the same path were used as in the example ("v:\\workspace\\Archives\\src\\archive_me"), the zipfile would contain "archive_me\\groucho" "archive_me\\harpo" and "archive_me\\chico."
Note that zipfile.namelist() always uses forward slashes in what it returns, a fact you will need to accommodate when comparing observed and expected.

The base directory ("archive_me" in the example above) is the final element of the input, and all paths recorded in the zipfile should start with the base directory.

If the directory contains subdirectories, the subdirectory names and any files in the subdirectories should not be included. (Hint: You can use isfile() to determine if a filename represents a regular file and not a directory.)

##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################

import os
import zipfile
import glob

def archdir(dir):
    zf = zipfile.ZipFile("zipped_up.zip", "w", zipfile.ZIP_DEFLATED)
    all_items = glob.glob(os.path.join(dir, "*"))
    base_dir = os.path.basename(dir)
    for item in all_items:
        filename = os.path.basename(item)
        if os.path.isfile(item) and filename != "zipped_up.zip":
            zf.write(item, os.path.join(base_dir, filename))      
    zf.close()
