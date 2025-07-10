import os

class ForkRoot(): # Работаем с forkmanager рут
    @staticmethod
    def get_root() -> str:
        WINDOWS_PATH = "%USERPROFILE%/.forkmanager" # Стандартный путь для винды
        return WINDOWS_PATH

    @staticmethod
    def open_workspaces() -> None:
        os.path.join(ForkRoot.get_root() + "workspaces") # Присоеденяем

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
        pass
