import spur
import spur.ssh

from st2actions.runners.pythonrunner import Action


class RoshAction(Action):
    def __init__(self, config):
        super(RoshAction, self).__init__(config=config)

    def run(self, **kargs):
        print(kargs)
        self.logger.info('Begin Action rosh')
        #get hpsa info from configuration
        config = self.config['hpsa']

        shell = spur.SshShell(
            hostname=config['admin_username'],
            port=int(config['ogfs_port']),
            username=config['username'],
            password=config['password'],
            connect_timeout=kwargs['timeout'],
            missing_host_key=spur.ssh.MissingHostKey.accept
        )
        command = "echo rosh -n %s -l %s %s" % (kwargs['target_hostname'], kwargs['run_as_username'], kwargs['run_command'])
        result = {}
        with shell:
            try:
                result = shell.run(command.split())
            except:
                raise
            else:
                return result.output
