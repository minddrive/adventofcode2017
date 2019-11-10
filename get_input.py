"""
Basic shared function to read input data for each problem; the data file
must be in the subdirectory 'input' and with the name '<prog_name>.txt',
where '<prog_name>.py' is the name of the program being run
"""

import inspect
import pathlib


def get_input():
    """
    Get input data for currently running program

    If the name of the program is '<prog_name>.py', then the data file
    must be 'input/<prog_name>.txt'

    Returns data from file, stripped of last newline
    """

    frame = inspect.stack()[1]
    filename = pathlib.Path(frame[0].f_code.co_filename)
    input_filename = pathlib.Path('input') / filename.with_suffix('.txt')

    with open(input_filename) as fh:
        input_data = fh.read().strip()

    return input_data
