import click
from utils import user_input, file_input, echo_with_check_new_line


@click.command()
@click.argument("paths", nargs=-1, type=click.Path())
def nl(paths):
    """A utility that numbers lines from a file."""

    pos = 0

    def echo_nl(input):
        nonlocal pos
        for line in input:
            pos += 1
            echo_with_check_new_line("{:6}".format(pos) + "\t" + line)

    if paths:
        for path in paths:
            echo_nl(file_input(path))
    else:
        echo_nl(user_input())


if __name__ == "__main__":
    nl()
