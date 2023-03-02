import textwrap
import time


def write_user_args(
    input_file: str,
    output_file: str,
    plot: str
):
    """
    Function to print user arguments to stdout
    """
    print(
        textwrap.dedent(
            f"""\
    -------------
    | Arguments |
    -------------
    Input file: {input_file}
    Output prefix: {output_file}.txt
    Plot: {plot if plot else False}
    """
        )
    )


def write_output_message(input_contents, merged_df, start_time):
    """
    Function to print out that the output files are being written
    """
    top_genes = merged_df[0:5]
    print(
        textwrap.dedent(
            f"""\

        -----------------------
        | Summary information |
        -----------------------
        Number of genes analyses: {len(input_contents)}
        Five highest ranked: {", ".join([gene[0] for gene in top_genes])}

        Execution time: {round(time.time() - start_time, 3)}s
    """
        )
    )

