import unittest
from remoterun import remoterun

class RemoteRunInitTest(unittest.TestCase):

    def test_remoterun_init(self):
        remoterun.init()
        from os.path import exists
        self.assertTrue(exists('.remoterunignore'))
        self.assertTrue(exists('.remoterunrc'))