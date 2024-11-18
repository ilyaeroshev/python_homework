import click
from utils import user_input, file_input


@click.command()
@click.argument("paths", nargs=-1, type=click.Path())
def wc(paths):
    """A utility that counts the number of lines, words, and bytes."""

    def calc_stat(input):
        line_cnt, word_cnt, char_cnt = 0, 0, 0
        for line in input:
            line_cnt += 1
            char_cnt += len(bytes(line, encoding="utf8"))
            for word in line.split():
                word_cnt += 1
        return line_cnt, word_cnt, char_cnt

    if paths:
        line_total_cnt, word_total_cnt, char_total_cnt = 0, 0, 0
        for path in paths:
            line_cnt, word_cnt, char_cnt = calc_stat(file_input(path))
            click.echo("{:8}{:8}{:8} {}".format(line_cnt, word_cnt, char_cnt, path))
            line_total_cnt += line_cnt
            word_total_cnt += word_cnt
            char_total_cnt += char_cnt
        if len(paths) > 1:
            click.echo(
                "{:8}{:8}{:8} total".format(
                    line_total_cnt, word_total_cnt, char_total_cnt
                )
            )
    else:
        line_cnt, word_cnt, char_cnt = calc_stat(user_input())
        click.echo("{:8}{:8}{:8}".format(line_cnt, word_cnt, char_cnt))


if __name__ == "__main__":
    wc()
