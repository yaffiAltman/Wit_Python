import click

from wit import Wit


class Cli:
    def __init__(self):
        self.wit = Wit()

    def create_cli(self):
        @click.group()
        def cli():
            pass
        cli()
        cli.add_command(self.init_cmd, name='init')
        cli.add_command(self.add_cmd, name='add')
        cli.add_command(self.log_cmd, name='log')
        cli.add_command(self.status_cmd, name='status')
        cli.add_command(self.checkout_cmd, name='checkout')
        cli.add_command(self.commit_cmd, name='commit')

    @click.command()
    def init_cmd(self):
        self.wit.init()

    @click.command()
    @click.argument('file_name')
    def add_cmd(self, file_name):
        self.wit.add(file_name)

    @click.command()
    def log_cmd(self):
        self.wit.log()

    @click.command()
    def status_cmd(self):
        self.wit.status()

    @click.command()
    @click.argument('commit_id')
    def checkout_cmd(self, commit_id):
        self.wit.checkout(commit_id)

    @click.command()
    @click.argument('message')
    def commit_cmd(self, message):
        self.wit.commit(message)
