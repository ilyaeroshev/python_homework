import click
from sys import stdin


def user_input():
    while line := stdin.readline():
        yield line


def file_input(path):
    with open(path) as file:
        while line := file.readline():
            yield line


def echo_with_check_new_line(line: str):
    click.echo(line, nl=(line and line[-1] != "\n"))
