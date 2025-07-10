import os
import json
import pathlib

class ForkRoot():  # Работаем с forkmanager рут
    @staticmethod
    def get_root() -> str:
        return os.path.join(os.path.expanduser("~"), ".forkmanager")

    @staticmethod
    def open_workspaces() -> None:

        # Простите я тут юзнул нейросеть потому что хуй
        # Chdir не работает нормально
        forkmanager_path = ForkRoot.get_root()
        os.makedirs(forkmanager_path, exist_ok=True)
        os.chdir(forkmanager_path)
        os.chdir("workspaces")
        pathlib.WindowsPath(forkmanager_path)

    @staticmethod
    def add_workspace(**attrs) -> bool:
        """
        Схема создания рабочего пространства:

        - Создание внешней директории
        - Заполнение конфига пространства
        - Создание проекта.
        - Включение пространства в json конфиг

        функция возвращает тру если все удалось
        функция возвращает фолс если были ошибки  
        """
        workspace_json = {
            "project_name": attrs["name"],
            "workspace_name": attrs["workspace"],
            "toml-settings": {
                "main_file": f"{attrs['name']}/src/__main__.py",
            }
        }

        ForkRoot.open_workspaces()
        os.mkdir(workspace_json["workspace_name"])
        os.chdir(workspace_json["workspace_name"])

        with open("workspace.json", "w") as workspace:
            json.dump(workspace_json, fp=workspace)

        os.mkdir(workspace_json["project_name"])
        os.chdir(workspace_json["project_name"])

        os.mkdir(f"{workspace_json["project_name"]}/src")

        source_dir = f"{workspace_json['project_name']}/src"

        with open(f"fork-project.lock", "w") as lock:
            lock.writelines(f"""
            [[project]]
            main_file="{workspace_json['toml-settings']['main_file']}"
            """)

        with open(f"{source_dir}/src/__main__.py", "w") as main:
            main.writelines("""
            def main():
                print("Hello!")
            main()
            """)

        return True
