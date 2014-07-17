Here are your instructions:

Make a TestDrivenDevelopment_Homework project and assign it to the Python2_Homework working set.
 Copy the setupDemo.py file from the TestDrivenDevelopment/src folder to the TestDrivenDevelopment_Homework/src folder.

 Modify it so that:
• The test_1() method includes code to verify that the test directory contains only the files created by the for loop. Hint: You might create a set containing the list of three filenames, and then create a set from the os.listdir() method.
•A test_3() method creates a binary file that contains exactly a million bytes, closes it and then uses os.stat to verify that the file on disk is of the correct length (with os.stat, statinfo.st_size returns the size in bytes).

##############################################################################################################################################################################################################################################################################################################################################3

"""
Demonstration of setUp and tearDown.
The tests do not actually test anything - this is a demo.
"""
import unittest
import tempfile
import shutil
import glob
import os

class FileTest(unittest.TestCase):
    
    def setUp(self):
        self.origdir = os.getcwd()
        self.dirname = tempfile.mkdtemp("testdir")
        
        os.chdir(self.dirname)
        
    def test_1(self):
        "Verify creation of files is possible"
        filenames = {"this.txt", "that.txt", "the_other.txt"}
        for filename in filenames:
            f = open(filename, "w")
            f.write("Some text \n")
            f.close()
            self.assertTrue(f.closed)
        dir_names = set(os.listdir('.')) 
        self.assertEqual(dir_names, filenames)
            
    def test_2(self):
        "Verify that the current directory is empty"
        self.assertEqual(glob.glob("*"), [],"Directory empty")
    
    def test_3(self):
        f = open("test.it", "wb") 
        filesize = (b'b'*1000000) 
        f.write(filesize) 
        f.close() 
        statinfo = os.stat("test.it")
        size =  statinfo.st_size * b'b'
        self.assertEqual(size, filesize) 
        
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.dirname)
       
        
if __name__ == "__main__":
    unittest.main()
