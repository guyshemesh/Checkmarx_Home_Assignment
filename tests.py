import unittest
from main import numpy_hello_world

class Test(unittest.TestCase):
    def test_numpy_hello_world(self):
        result = numpy_hello_world()
        self.assertEqual(result,"Hello World!")

if __name__ == '__main__':
    unittest.main()
