# PyConsole
Console, same as 'win + r -> cmd', but with ability to make custom commands.

AND!!! This Console has my own test data keeper, such as json, but much easier.

## Class Command, which need to make your own command:
```py
Command(name: str, desc: str, action)
# action - your function with list in arguments
```

## Example:
```py
def MyCommandAction(args: list):
  print(f"args - {args}")
```

You need to add your command to 'commands' list in commands.py
```py
commands = [
  Command('your_command_keyword', 'your command description', MyCommandAction)
]
```

## Result:
```
OkeConsole> your_command_keyword arg1 arg2
args - ['arg1', 'arg2']
```

  
