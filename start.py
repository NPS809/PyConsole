from CommandHandler.main import CommandHandlerThread
from DataManager.main import *
import os

app_info = Chapter("app_info")
update_logs = Chapter("update_logs")

os.system("title OkeConsole")
os.system("cls")

print(f"{app_info.Get("names")} v{list(update_logs.GetCellsDict().keys())[-1]}")
CommandHandlerThread()