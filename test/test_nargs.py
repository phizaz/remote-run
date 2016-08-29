import unittest
from remoterun import utils

class NargsTest(unittest.TestCase):

    def test_nargs(self):

        import sys
        utils.run_command_attach_output([
            sys.executable, 'test_nargs_app.py', 'a', 'b'
        ])

        utils.run_command_attach_output([
            sys.executable, 'test_nargs_app.py'
        ])