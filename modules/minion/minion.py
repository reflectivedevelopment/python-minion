import argparse
import sys

def factory():
    return minion()

class minion():
    def execute(self):
        parser = argparse.ArgumentParser(description='Minion Tool for doing all your python tasks')
        parser.add_argument('--url', default='minion')
        parser.add_argument('--task', default=None)

        args, unknown = parser.parse_known_args()

        if args.task is None:
            raise Exception('Task cannot be left blank.')
        print args
        print unknown
