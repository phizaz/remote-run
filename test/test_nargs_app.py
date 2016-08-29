import argparse

parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
parser.add_argument('--tmp')
args = parser.parse_args()

print(args)