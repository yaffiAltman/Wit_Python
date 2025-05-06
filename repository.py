# from wit import Wit
# import click
#
#
# # class Repository:
# wit_instance = Wit()
#
# # def __init__(self):
# #     self.cli()
#
# @staticmethod
# @click.group()
# def cli():
#     pass
#
# @classmethod
# @click.command()
# def init_cmd(cls):
#     cls.wit_instance.init()
#
# @classmethod
# @click.command()
# @click.argument('file_name')
# def add_cmd(cls, file_name):
#     cls.wit_instance.add(file_name)
#
# @classmethod
# @click.command()
# def log_cmd(cls):
#     cls.wit_instance.log()
#
# @classmethod
# @click.command()
# def status_cmd(cls):
#     cls.wit_instance.status()
#
# @classmethod
# @click.command()
# @click.argument('commit_id')
# def checkout_cmd(cls, commit_id):
#     cls.wit_instance.checkout(commit_id)
#
# @classmethod
# @click.command()
# @click.argument('message')
# def commit_cmd(cls, message):
#     cls.wit_instance.commit(message)
#
# cli.add_command(init_cmd, name='init')
# cli.add_command(add_cmd, name='add')
# cli.add_command(log_cmd, name='log')
# cli.add_command(status_cmd, name='status')
# cli.add_command(checkout_cmd, name='checkout')
# cli.add_command(commit_cmd, name='commit')


from wit import Wit
import click


class Repository:
    wit_instance = Wit()

    @staticmethod
    @click.group()
    def cli():
        pass

    @classmethod
    @click.command()
    def init_cmd(cls):
        cls.wit_instance.init()

    @classmethod
    @click.command()
    @click.argument('file_name')
    def add_cmd(cls, file_name):
        cls.wit_instance.add(file_name)

    @classmethod
    @click.command()
    def log_cmd(cls):
        cls.wit_instance.log()

    @classmethod
    @click.command()
    def status_cmd(cls):
        cls.wit_instance.status()

    @classmethod
    @click.command()
    @click.argument('commit_id')
    def checkout_cmd(cls, commit_id):
        cls.wit_instance.checkout(commit_id)

    @classmethod
    @click.command()
    @click.argument('message')
    def commit_cmd(cls, message):
        cls.wit_instance.commit(message)


# Add commands to cli
Repository.cli.add_command(Repository.init_cmd, name='init')
Repository.cli.add_command(Repository.add_cmd, name='add')
Repository.cli.add_command(Repository.log_cmd, name='log')
Repository.cli.add_command(Repository.status_cmd, name='status')
Repository.cli.add_command(Repository.checkout_cmd, name='checkout')
Repository.cli.add_command(Repository.commit_cmd, name='commit')

if __name__ == '__main__':
    Repository.cli()
