import os

class ForkRoot(): # Работаем с forkmanager рут
    @staticmethod
    def open_root() -> None:
        WINDOWS_PATH = "%USERPROFILE%/.forkmanager" # Стандартный путь для винды

        os.path.join(WINDOWS_PATH)

    @staticmethod
    def add_workspace(**attrs) -> bool:
        return True     # Пока еще не сдеолано продолжу завтра
