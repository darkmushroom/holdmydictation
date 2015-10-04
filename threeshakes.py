import unittest
import darkIO
import os.path

class TestHMDict(unittest.TestCase):

    def test_saves_file_by_name(self):
        darkIO.DarkIO.save("filename.txt","This is some test text")
        print(os.path)
        self.assertTrue(os.path.isfile("filename.txt"))        
        os.remove("filename.txt")

if __name__ == '__main__':
	unittest.main()
