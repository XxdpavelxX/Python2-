import archiver
import unittest
import shutil
import os
import zipfile
import tempfile

class TestRelativezip(unittest.TestCase):
    def setUp(self):
        self.origdir = os.getcwd()
        self.tempdir = tempfile.mkdtemp("test_relative_zip")
        os.chdir(self.tempdir)
        os.mkdir("archive_me")
        filenames = ["groucho", "harpo", "chico"]
        for fn in filenames:
            f = open(fn, "w")
            f.close()
        base_dir = os.path.basename(self.tempdir)
        self.fixture_files = set(["/".join([base_dir, fn]) for fn in filenames])
 
    def test_zip_up(self):
        archiver.archdir(self.tempdir)
        zf = zipfile.ZipFile("zipped_up.zip")
        zipped_files = set([fn for fn in zf.namelist()])
        zf.close()
        self.assertEqual(zipped_files, self.fixture_files)  
 
    def tearDown(self):
        os.chdir(self.origdir)
        shutil.rmtree(self.tempdir)
 
if __name__ == "__main__":
    unittest.main()

