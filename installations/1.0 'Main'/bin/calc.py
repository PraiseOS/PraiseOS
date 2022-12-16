
def description():
    return "Calculates Values That Are Given Upon Execution"

def run(cmd):
    try:
        print(eval(cmd.removeprefix('calc ').replace('"', '').removesuffix('calc')))
    except:
        print('Inproper Equation')