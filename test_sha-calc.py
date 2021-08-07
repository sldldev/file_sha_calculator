from unittest import TestCase

from modules.shacalc import get_sha256


class Test(TestCase):

    def test_get_sha256(self):
        test_file = r"EMPTY_TEST_FILE.txt"
        res = get_sha256(test_file)
        self.assertTrue(isinstance(res, list))
        self.assertTrue(len(res) == 32)
        print(res)
