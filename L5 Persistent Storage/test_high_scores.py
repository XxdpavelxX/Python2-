import unittest
import shelve
import os
from high_scores import Scores
 
class Test_Scores(unittest.TestCase):
    
    def test_interactive(self):
    
        mydict=['Pavel' , 'David' , 'Pavel', 'David','David']
        score=[20,20,10,50,-23]
        expectedResult=[20,20,20,50,50]
        x=0
        for name in mydict:       
            result=Scores(name,score[x])
            print (name ,result,expectedResult[x])
            
            self.assertEqual(result,expectedResult[x])
            x=x+1
        shelf = shelve.open(r'myshelf.shlf')
        self.assertEqual(shelf['Pavel'],20)
        self.assertEqual(shelf['David'],50)
        shelf.clear()
if __name__ == '__main__':
    unittest.main()
