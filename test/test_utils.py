from __future__ import print_function

from remoterun import utils
import unittest

class UtilsTest(unittest.TestCase):

    def test_source_dir(self):
        from os.path import basename, dirname
        path = utils.source_dir()
        print(path)
        self.assertEqual(basename(path), 'remoterun')
        self.assertEqual(basename(dirname(path)), 'remote-run')

    def test_caller_dir(self):
        from os.path import basename
        path = utils.caller_dir()
        print(path)
        self.assertEqual(basename(path), 'test')

    def test_load_save_lockfile(self):
        from os.path import exists
        from os import remove
        if exists(utils.path_lockfile()):
            remove(utils.path_lockfile())

        r = utils.load_lockfile()
        self.assertIsNone(r, None)

        r = utils.save_lockfile('aoeu')
        r = utils.load_lockfile()
        self.assertEqual(r, 'aoeu')

    def test_load_config(self):
        r = utils.load_config()
        print(r)

    def test_load_ignore(self):
        r = utils.load_ignore()
        print(r)
        self.assertListEqual(r, ['.remoterunignore', '.remoterunrc'])

    def test_run_command(self):
        r = utils.run_command_attach_output(['echo', 'test'])

        self.assertEqual(r, 0)

    def test_run_command_with_terminal(self):
        r = utils.run_command_with_terminal([
            'ssh', '-t', 'ta@192.168.1.45'
        ])
        print(r)


    def test_inject_vals(self):
        r = utils.inject_vals(dict(a=10, b=20))
        print(r)
        self.assertTrue('a' in r)
        self.assertTrue('b' in r)
        self.assertTrue('arg' in r)