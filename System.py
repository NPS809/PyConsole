from colorama import Fore, init
import os


def Cls(args: list):
    os.system("cls")


def Echo(args: list):
    if len(args) > 0:
        print(*args)
    else:
        print("echo [your text]")


def Color(args: list):
    if len(args) > 1:
        print("color command must have 1 argument!")
    else:
        os.system(f"color {args[0]}")

def Exit(args: list):
    exit()
