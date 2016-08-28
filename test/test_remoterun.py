from __future__ import print_function

import unittest

from remoterun.remoterun import *
from remoterun import utils


class RemoteRunTest(unittest.TestCase):
    def test_run_local(self):
        conf = utils.load_config()
        print(conf)
        run_local(['echo', 'test', '{host}'], conf)

    def test_run_remote(self):
        conf = utils.load_config()
        print(conf)
        run_remote(['echo', 'test', '{host}'], conf)

    def test_run(self):
        run()

    def test_format(self):
        l = [1, 2, 3]
        s = '{l[0]}'.format(l=l)
        print(s)

