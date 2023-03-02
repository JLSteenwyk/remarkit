import sys
import textwrap

from argparse import (
    ArgumentParser,
    SUPPRESS,
    RawDescriptionHelpFormatter,
)

from .version import __version__

def create_parser():
    parser = ArgumentParser(
        add_help=False,
        formatter_class=RawDescriptionHelpFormatter,
        usage=SUPPRESS,
        description=textwrap.dedent(
            f"""\
             _____      __  __            _  _______ _______ 
            |  __ \    |  \/  |          | |/ /_   _|__   __|
            | |__) |___| \  / | __ _ _ __| ' /  | |    | |   
            |  _  // _ \ |\/| |/ _` | '__|  <   | |    | |   
            | | \ \  __/ |  | | (_| | |  | . \ _| |_   | |   
            |_|  \_\___|_|  |_|\__,_|_|  |_|\_\_____|  |_|   
                                                  

        Version: {__version__}
        Citation: Steenwyk et al. 2023, JOURNAL. doi: 10.1371/journal.pbio.3001007
        https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3001007

        ReMarKIT uses machine learning and information theory.

        Usage: remarkit <input> [optional arguments]
        """
        ),
    )

    # if no arguments are given, print help and exit
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit()

    ## required arguments
    required = parser.add_argument_group(
        "required arguments",
        description=textwrap.dedent(
            """\
        <input>                                     input file
                                                    (must be the first argument)
        """
        ),
    )

    required.add_argument("input", type=str, help=SUPPRESS)

    ## optional arguments
    optional = parser.add_argument_group(
        "optional arguments",
        description=textwrap.dedent(
            """\
        -o, --output <output_file_name>             output file name 
                                                    (default: input file named with '.remarkit' suffix)

        -p, --plot <plot_results>                   plot ReMarKIT results
                                                    (default: off)
 
        -h, --help                                  help message
        -v, --version                               print version

        -------------------------------------
        | Detailed explanation of arguments | 
        -------------------------------------
        Input
            - input must be a three column file
            - column 1: locus identifier
            - column 2: path to alignment in FASTA format
            - column 3: path to tree file in Newick format

        Output
            - prefix of output file names

        Plot
            - generates plots of results 
            
        """
        ),
    )

    optional.add_argument(
        "-o", "--output", help=SUPPRESS, metavar="output"
    )

    output_formats = [output_format for output_format in ["svg", "png"]]
    optional.add_argument(
        "-p", "--plot", help=SUPPRESS, metavar="output", choices=output_formats
    )

    optional.add_argument(
        "-h", "--help", action="help", help=SUPPRESS,
    )

    optional.add_argument(
        "-v", "--version", action="version", version=f"remarkit {__version__}", help=SUPPRESS,
    )

    return parser
