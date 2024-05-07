from dm import Chapter
from colorama import Fore, init
import os

app_info = Chapter("app_info")
update_logs = Chapter("update_logs")


def Cls(args: list):
    os.system("cls")


def Echo(args: list):
    if len(args) > 0:
        print(*args)
    else:
        print("echo [your text]")


def UpdateLog(args: list):
    udplog = list(update_logs.GetCellsDict().keys())[-1]
    print(f'Last update: {Fore.GREEN}v{udplog}{Fore.WHITE}\n', "Update history:\n", sep="")
    for version, log in update_logs.GetCellsDict().items():
        print(f"{Fore.GREEN}v{version}{Fore.WHITE}:\n{log.strip()}\n")


def Color(args: list):
    if len(args) > 1:
        print("color command must have 1 argument!")
    else:
        os.system(f"color {args[0]}")

def Exit(args: list):
    exit()
