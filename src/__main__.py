import os

import click

from utils.forkutil import ForkRoot
from utils.textutil import *

@click.group()  # Основная группа с командами
def clipr():
    pass

@clipr.command()
@click.argument('project_name')
def create(project_name: str) -> None:
    os.path.join(ForkRoot.get_root()) # Открываем fork-root

    workspace_name = make_str(project_name)

    ForkRoot.add_workspace(
        name=project_name,
        workspace=workspace_name # Имя workspace
    )

if __name__ == "__main__":
    clipr()
