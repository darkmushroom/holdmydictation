import unittest
import darkIO
import os.path


class TestHMDict(unittest.TestCase):
    def test_saves_file_by_name(self):
        darkIO.DarkIO.save("filename.txt", "This is some test text")
        self.assertTrue(os.path.isfile("filename.txt"))

    def test_loads_file_by_name(self):
        darkIO.DarkIO.save("filename.txt", "This is some test text")
        self.assertEqual(darkIO.DarkIO.load("filename.txt"),
                         "This is some test text")

    def tearDown(self):

        os.remove("filename.txt")


if __name__ == '__main__':
    unittest.main()
