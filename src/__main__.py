import os

from utils.forkutil import ForkRoot

import click

@click.group()  # Основная группа с командами
def clipr():
    pass

@clipr.command()
@click.argument('project name')
def create(project_name: str) -> None:
    ForkRoot.open_root() # Открываем fork-root
    ForkRoot.add_workspace(name=project_name)
