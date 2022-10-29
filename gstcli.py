from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

input_console = Console(stderr=False)

def displayHelp():
    input_console.print('List of GSTNs')
    input_console.print('list')

def exit():
    input_console.print('Thanks for spending your time in this application. Help us improve so that we can save your time.')
    quit()

if __name__ == '__main__':
    p5 = lambda rsstr : int(20*float(rsstr))
    while True:
        cmd = Prompt.ask("₹")
        # argLst = cmd.split(sep=' ')
        match cmd.split():
            case [ 'help' ]:
                displayHelp()
            case [ 'exit' ]:
                exit()