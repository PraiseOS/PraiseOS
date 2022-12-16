
def run(cmd):
    with open(cmd.removeprefix('touch ').replace('"', '').removesuffix('touch')) as f:
        f.write("")