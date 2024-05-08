import os


class BaseCommands:
    @staticmethod
    def Clear(args: list):
        os.system("cls")

    @staticmethod
    def Echo(args: list):
        if len(args) > 0:
            print(*args)
        else:
            print("echo [your text]")

    @staticmethod
    def Color(args: list):
        if len(args) > 1:
            print("color command must have 1 argument!")
        else:
            os.system(f"color {args[0]}")

    @staticmethod
    def Exit(args: list):
        exit()


class Command:
    def __init__(self, name: str, desc: str, action):
        self.name = name
        self.description = desc
        self.action = action


def Help(args: list):
    for comm in commands:
        print(f"{comm.name}{(15 - len(comm.name)) * " "}{comm.description}")


commands = [
    Command("cls", "Выполняет очистку экрана", BaseCommands.Clear),
    Command("echo", "Выводит заданный текст на экран консоли", BaseCommands.Echo),
    Command("help", "Список всех доступных команд", Help),
    Command("exit", "Выход из приложения", BaseCommands.Exit),
    Command("color", "Настроить цвет текста и фона в консоли", BaseCommands.Color)
]
