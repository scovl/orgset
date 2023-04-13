import unittest
from orgset import OrgSet

class OrgSetTestCase(unittest.TestCase):

    def setUp(self):
        self.orgset = OrgSet()

    def test_check_os(self):
        self.orgset.check_os()
        self.assertIn(self.orgset.os_type, ["Linux", "Windows", "MacOS"])


if __name__ == '__main__':
    unittest.main()
