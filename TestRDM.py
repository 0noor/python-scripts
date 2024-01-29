import rdm
import unittest


class TestRdm(unittest.TestCase):
    def test_ran(self):
        answer = 5
        guess = 5
        result = rdm.ran(answer, guess)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
