
def run(cmd):

    file = cmd.removeprefix('cat ').replace('"', '').removesuffix('cat')

    with open(file) as f:
        text = f.read()

    print(text)