Here are your instructions:

Make a UnitTesting_Homework project and assign it to the Python2_Homework working set. In this project, write a unittest test program for the following function.
 (The test program makes unittest.TestCase assertions about the results of calling the function with known arguments.)

def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]Test your results for a given string s by comparing them with s.title().

 Because this is purely an exercise it's OK to put your test code in the same file as the function and just hand in a single file.
 Your file should be an importable module.

 You should be able to find an example that shows title(s) and s.title() diverge (have different output).

###############################################################################################################################################################################################################################

import unittest

def title(s):
    "How close is this function to str.title()?"
    return s[0].upper()+s[1:]

class Testtitle(unittest.TestCase):
    def test_title(self):
        s = 'little Red Riding Hood'
        self.assertEqual(title(s),s.title(), "First letter should be capitalized")
    def test_bad_input(self):
        self.assertRaises(TypeError, title, 123)
if __name__ == "__main__":
    unittest.main()
