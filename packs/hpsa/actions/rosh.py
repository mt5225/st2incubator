import spur
import spur.ssh

from st2actions.runners.pythonrunner import Action


class RoshAction(Action):
    def __init__(self, config):
        super(RoshAction, self).__init__(config=config)

    def run(self, **kwargs):
        self.logger.info(kwargs)
        #get hpsa info from configuration
        config = self.config['hpsa']

        shell = spur.SshShell(
            hostname=config['ogfs_host'],
            port=int(config['ogfs_port']),
            username=config['admin_username'],
            password=config['admin_password'],
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
