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

        task_period = args.task.replace(':','.')
        task_under = args.task.replace(':','_')

        task_module = __import__( 'classes.task.%s' % task_period, fromlist=[task_under])

        task_class = getattr(task_module, 'minion_task_%s' % task_under)

        task = task_class()

        task_parser = argparse.ArgumentParser(description='Minion Tool for doing all your python tasks')

        task_args = {}

        if len(task._config) > 0:
            for conf in task._config:
                task_parser.add_argument('--%s' % conf, action='append', default=[], nargs='?')

            task_args, unknown = task_parser.parse_known_args()

            task_args = vars(task_args)

        task.execute(task_args)
