from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console
from rich import box
import common

input_console = Console(stderr=False)

def displayHelp():
    table = Table(title=f"Help", box=box.HORIZONTALS)

    table.add_column("Help", justify="left", style="medium_purple3")
    table.add_column("Command", justify="left", style="light_steel_blue1")
    cmds = {"Help": "help",
            "List of GSTNs" : "list",
            "Exit": "exit"}
    for c in cmds:
        table.add_row(f"{c}",f"{cmds[c]}")
    input_console.print(table)

def exit():
    input_console.print('Thanks for spending your time in this application. Help us improve so that we can save your time.')
    quit()

def listGSTNs():
    table = Table(title=f"GSTNs", box=box.HORIZONTALS)

    table.add_column("User-id", justify="left", style="medium_purple3")
    table.add_column("GST No.", justify="left", style="light_steel_blue1")
    for g in common.readConfig('gst'):
        for i in g:
            table.add_row(f"{i}",f"{g[i]}")
    input_console.print(table)

if __name__ == '__main__':
    p5 = lambda rsstr : int(20*float(rsstr))
    while True:
        cmd = Prompt.ask("₹")
        match cmd.split():
            case [ 'help' ]:
                displayHelp()
            case [ 'exit' ]:
                exit()
            case [ 'list' ]:
                listGSTNs()