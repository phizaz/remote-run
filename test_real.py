from __future__ import print_function

import unittest
from remoterun import utils

class RemoteRunRealTest(unittest.TestCase):

    def test_real_init(self):
        import sys
        from os.path import join

        self.assertRaises(Exception, utils.run_command_attach_output, [
            sys.executable, '-m', 'remoterun'
        ])

        utils.run_command_attach_output([
            sys.executable, '-m', 'remoterun', '--init'
        ])

        from os.path import exists
        from os import remove

        self.assertTrue(exists('.remoterunignore'))
        self.assertTrue(exists('.remoterunrc'))

        remove('.remoterunignore')
        remove('.remoterunrc')
        try:
            remove('.remoterun_lock')
        except Exception:
            pass

    def test_real_run(self):
        import sys
        from shutil import copy

        copy('test/.remoterunignore', utils.path_ignorefile())
        copy('test/.remoterunrc', utils.path_config())

        utils.run_command_attach_output([
            sys.executable, '-m', 'remoterun'
        ])

        from os import remove
        remove('.remoterunignore')
        remove('.remoterunrc')
