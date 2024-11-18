import click
from utils import user_input, file_input, echo_with_check_new_line


@click.command()
@click.argument("paths", nargs=-1, type=click.Path())
def tail(paths):
    """A utility that outputs the last 10 lines from files."""

    def ring_iterator(ring_size, start=0):
        i = start
        while True:
            yield i
            i = (i + 1) % ring_size

    def fill_ring_buffer(buf_size, input):
        ring_buf = [None for _ in range(buf_size)]
        it = ring_iterator(buf_size)
        pos = next(it)  # позиция вставки

        for line in input:
            ring_buf[pos] = line
            pos = next(it)

        return ring_buf, pos

    def echo_ring_buffer(buf_size, end=0):
        it = ring_iterator(buf_size, end)
        i = next(it)
        while True:
            if ring_buf[i] is not None:
                echo_with_check_new_line(ring_buf[i])
            i = next(it)
            if i == end:
                break

    if paths:
        buf_size = 10
        first_output = True

        for path in paths:
            ring_buf, pos = fill_ring_buffer(buf_size, file_input(path))

            if not first_output:
                click.echo()
            else:
                first_output = False

            if len(paths) > 1:
                click.echo("==> " + path + " <==")

            echo_ring_buffer(buf_size, pos)
    else:
        buf_size = 17

        ring_buf, pos = fill_ring_buffer(buf_size, user_input())

        echo_ring_buffer(buf_size, pos)


if __name__ == "__main__":
    tail()
