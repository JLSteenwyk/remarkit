import logging
import os.path
import sys


logger = logging.getLogger(__name__)


def process_args(args) -> dict:
    """
    Process args from argparser and set defaults
    """
    input_file = args.input
    output_file = args.output or f"{input_file}.remarkit"

    if not os.path.isfile(input_file):
        logger.warning("Input file does not exist")
        sys.exit()

    if input_file == output_file:
        logger.warning("Input and output files can't have the same name.")
        sys.exit()

    # assign optional arguments
    plot = args.plot or False

    return dict(
        input_file=input_file,
        output_file=output_file,
        plot=plot,
    )
