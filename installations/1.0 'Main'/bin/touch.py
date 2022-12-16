
def run(cmd):
    with open(cmd.removeprefix('touch ').replace('"', '').removesuffix('touch'), 'w') as f:
        pass