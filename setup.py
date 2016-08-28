from __future__ import print_function
from setuptools import setup
from os.path import join, dirname, abspath
import re


def get_version_from(file):
    version = re.search(
        '^__version__\s*=\s*\'(.*)\'',
        open(file).read(),
        re.M
    ).group(1)
    return version


version = get_version_from(join(dirname(__file__), 'remoterun', 'remoterun.py'))

setup(
    name='remote-run',
    packages=['remoterun'],
    include_package_data=True,
    install_requires=[
        'future',
        'pyyaml'
    ],
    entry_points={
        "console_scripts": ['remoterun = remoterun.remoterun:main']
    },
    version=version,
    description='Running your script on a remote machine as if it were on your local one',
    author='Konpat Preechakul',
    author_email='the.akita.ta@gmail.com',
    url='https://github.com/phizaz/remote-run',  # use the URL to the github repo
    keywords=['remote', 'utility'],  # arbitrary keywords
    classifiers=[],
)
