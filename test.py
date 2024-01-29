import unittest
import testmain

class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = testmain.do_stuff(test_param)
        self.assertEqual(result, 15)

unittest.main()
