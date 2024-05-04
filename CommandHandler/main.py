from CommandHandler.commands import commands


def CommandHandlerThread():
    while True:
        ui = input(f"\nOkeConsole>")
        if ui.replace(" ", "") != "":
            tmp = CommandCutter(ui)
            CommandExecuter(tmp["command"], tmp["args"])


def CommandCutter(ui: str):
    words = ui.split(" ")
    while "" in words: words.remove("")
    command = words[0]
    words.pop(0)
    return {"command": command, "args": words}


def CommandExecuter(command: str, args: list):
    for com in commands:
        if com.name == command:
            com.action(args)
            return
    print(f"Команды '{command}' не существует. Чтобы посмотреть список доступных команд, напишите 'help'")
