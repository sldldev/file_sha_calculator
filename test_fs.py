import os
from unittest import TestCase

from file_sha_calculator.fs import create_path,SAFE_LOC


class Test(TestCase):
    def test_create_folder(self):
        hex_list = ['e3', 'b0', 'c4', '42', '98', 'fc', '1c', '14', '9a', 'fb', 'f4', 'c8', '99', '6f', 'b9', '24',
                    '27', 'ae', '41', 'e4', '64', '9b', '93', '4c', 'a4', '95', '99', '1b', '78', '52', 'b8', '55']
        path = create_path(hex_list)
        print (path)
        print (os.path.join(SAFE_LOC, "\\".join(hex_list[0: len(hex_list)-1])))
        self.assertTrue(path == os.path.join(SAFE_LOC, "\\".join(hex_list[0: len(hex_list)-1])))
        self.assertTrue(os.path.exists(os.path.join(SAFE_LOC, "\\".join(hex_list[0: len(hex_list)-1]))))

