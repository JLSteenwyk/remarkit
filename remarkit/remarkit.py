#!/usr/bin/env python

import logging
import sys
import time

from .args_processing import process_args
from .files import (
    read_input_file,
    output_information_content,
    output_plot,
)
from .info_content_calc import (
    calculate_desirabilities,
    create_info_content_matrices,
)
from .parser import create_parser
from .write import write_user_args, write_output_message

logger = logging.getLogger(__name__)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)


def execute(
    input_file: str,
    output_file: str,
    plot: bool,
):
    """
    Master execute Function                                      
    This function executes the main functions and calls other    
    subfunctions to trim the input file  
    """
    write_user_args(input_file, output_file, plot)

    start_time = time.time()

    input_contents = read_input_file(input_file)

    identifiers, treeness_over_rcv, saturation, treeness = create_info_content_matrices(input_contents)

    merged_df = calculate_desirabilities(identifiers, treeness_over_rcv, saturation, treeness)

    output_information_content(merged_df, output_file)

    if plot:
        output_plot(merged_df, output_file, plot)

    write_output_message(input_contents, merged_df, start_time)
    

def main(argv=None):
    """
    Function that parses and collects arguments              
    """
    # parse and assign arguments
    parser = create_parser()
    args = parser.parse_args()

    # pass to master execute function
    execute(**process_args(args))


if __name__ == "__main__":
    main(sys.argv[1:])
