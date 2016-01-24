import sys

from st2actions.runners.pythonrunner import Action


class RoshAction(Action):
    def run(self, **kargs):
        print(kargs)
        self.logger.info('Action successfully completed')
        sys.exit(0)
