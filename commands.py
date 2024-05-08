import System

class Command:
    def __init__(self, name: str, desc: str, action):
        self.name = name
        self.description = desc
        self.action = action


def Help(args: list):
    for comm in commands:
        print(f"{comm.name}{(15 - len(comm.name)) * " "}{comm.description}")


commands = [
    Command("cls", "Выполняет очистку экрана", System.Cls),
    Command("echo", "Выводит заданный текст на экран консоли", System.Echo),
    Command("help", "Список всех доступных команд", Help),
    Command("exit", "Выход из приложения", System.Exit),
    Command("color", "Настроить цвет текста и фона в консоли", System.Color)
]
