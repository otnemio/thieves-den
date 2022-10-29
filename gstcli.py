from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

input_console = Console(stderr=False)

def displayHelp():
    input_console.print('List of GSTNs')
    input_console.print('list')

if __name__ == '__main__':
    p5 = lambda rsstr : int(20*float(rsstr))
    while True:
        cmd = Prompt.ask("₹")
        argLst = cmd.split(sep=' ')
        if argLst[0] == 'help':
            displayHelp()