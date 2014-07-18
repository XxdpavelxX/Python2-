import unittest
import os
import tempfile
import shutil
from file_handling import filecount


class CounterTest(unittest.TestCase):
    def setUp(self):
        self.a= "testing_dir2"
        self.a=tempfile.mkdtemp()
        os.chdir(self.a)
        f = open('1.txt', "w")
        f.write("sadasfvsdter")
        f.close()
        g = open('2.txt',"w")
        g.write("asdsferterg")
        g.close()
        h = open('3.py',"w")
        h.write('fgdfgtry')
        h.close()
        i= open('4.doc',"w")
        i.write('fhghyhy')
        i.close()
        
    def test_counter(self):
        self.assertEqual(filecount(os.getcwd()),{'txt':2, 'py':1, 'doc':1})
        
    def test_simple_files_pat(self):
        "test a few simple files"
        from file_handling import filecount as file_count
        testdir = tempfile.mkdtemp("testdir")
        os.chdir(testdir)
        filenames=["file1.txt","file2.txt"]
        expected={'txt':2}
        for f in filenames:
            open(f, 'w').close()
        observed = file_count(os.getcwd())
        self.assertEqual(observed, expected,
                         "expected {}, but got {}.".format(expected, observed))
        
    def test_subdir_pat(self):
        "test a few simple files w a subdir"
        from file_handling import filecount as file_count
        testdir = tempfile.mkdtemp("testdir")
        os.chdir(testdir)
        os.mkdir('some.bogus.subdir')
        filenames=["file1.txt","file2.txt"]
        expected={'txt':2}
        for f in filenames:
            open(f, 'w').close()
        observed = file_count(os.getcwd())
        self.assertEqual(observed, expected,
                         "expected {}, but got {}.".format(expected, observed))
        
    def test_strange_files_pat(self):
        "test strange files"
        from solution import filecount as file_count
        testdir = tempfile.mkdtemp("testdir")
        os.chdir(testdir)
        filenames=["2014.March.17.log.txt","file2.txt"]
        expected={'txt':2}
        for f in filenames:
            open(f, 'w').close()    
        observed = file_count(os.getcwd())
        self.assertEqual(observed, expected,
                         "expected {}, but got {}.".format(expected, observed))
    
    def tearDown(self):
        pardir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
        os.chdir(pardir)
        shutil.rmtree(self.a)
 


        

         
if __name__ == "__main__":
    unittest.main()
    
