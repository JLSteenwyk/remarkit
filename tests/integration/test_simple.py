import imghdr
import os
from pathlib import Path

import pytest

from remarkit.remarkit import execute

here = Path(__file__)


@pytest.mark.integration
class TestRemarkit(object):
    def test_simple_default(self):
        """
        usage: remarkit ./tests/integration/samples/input_file_small.txt
        """
        output_file = "output/output"

        kwargs = dict(
            input_file=f"{here.parent}/samples/input_file_small.txt",
            output_file=output_file,
            plot=None,
        )

        execute(**kwargs)

        with open(
            f"{here.parent}/expected/output.txt", "r"
        ) as expected:
            expected_content = expected.read()

        with open(output_file+".txt", "r") as out_file:
            output_content = out_file.read()

        assert expected_content == output_content

    def test_simple_plot_png(self):
        """
        usage: remarkit ./tests/integration/samples/input_file_small.txt -p png
        """
        output_file = "output/output"

        kwargs = dict(
            input_file=f"{here.parent}/samples/input_file_small.txt",
            output_file=output_file,
            plot="png",
        )

        execute(**kwargs)

        assert os.path.isfile("output/output.png")
        assert imghdr.what("output/output.png") == "png"

    def test_simple_plot_svg(self):
        """
        usage: remarkit ./tests/integration/samples/input_file_small.txt -p svg
        """
        output_file = "output/output"

        kwargs = dict(
            input_file=f"{here.parent}/samples/input_file_small.txt",
            output_file=output_file,
            plot="svg",
        )

        execute(**kwargs)

        assert os.path.isfile("output/output.svg")





#     def test_simple_long_description_complement(self):
#         """
#         test complementary output file with a simple case
#         usage: remarkit simple_long_description.fa -c
#         """
#         output_file = "output/simple_long_description.fa_gappy"
#         complement_out_file = f"{output_file}.complement"

#         kwargs = dict(
#             input_file=f"{here.parent}/samples/simple_long_description.fa",
#             output_file=output_file,
#             input_file_format='fasta',
#             output_file_format='fasta',
#             complement=True,
#             gaps=0.9,
#             mode=TrimmingMode.gappy,
#             use_log=False,
#         )

#         execute(**kwargs)

#         with open(
#             f"{here.parent}/expected/simple_long_description.fa_gappy.complement", "r"
#         ) as expected:
#             expected_content = expected.read()

#         with open(complement_out_file, "r") as out_file:
#             output_content = out_file.read()

#         assert expected_content == output_content

#     def test_12_YIL115C_Anc_2_253_aa_aln_complement(self):
#         """
#         test complementary output file for amino acid yeast sequences
#         usage: remarkit 12_YIL115C_Anc_2.253_aa_aln.fasta -c
#         """
#         output_file = "output/12_YIL115C_Anc_2.253_aa_aln.fasta_gappy"
#         complement_out_file = f"{output_file}.complement"

#         kwargs = dict(
#             input_file=f"{here.parent}/samples/12_YIL115C_Anc_2.253_aa_aln.fasta",
#             output_file=output_file,
#             input_file_format='fasta',
#             output_file_format='fasta',
#             complement=True,
#             gaps=0.9,
#             mode=TrimmingMode.gappy,
#             use_log=False,
#         )
#         execute(**kwargs)

#         with open(
#             f"{here.parent}/expected/12_YIL115C_Anc_2.253_aa_aln.fasta_gappy.complement",
#             "r",
#         ) as expected:
#             expected_content = expected.read()

#         with open(complement_out_file, "r") as out_file:
#             output_content = out_file.read()

#         assert expected_content == output_content

#     def test_EOG091N44M8_aa_complement(self):
#         """
#         test complementary output file for amino acid Penicillium sequences
#         usage: remarkit EOG091N44M8_aa.fa -c
#         """
#         output_file = "output/EOG091N44M8_aa.fa_gappy"
#         complement_out_file = f"{output_file}.complement"

#         kwargs = dict(
#             input_file=f"{here.parent}/samples/EOG091N44M8_aa.fa",
#             output_file=output_file,
#             input_file_format='fasta',
#             output_file_format='fasta',
#             complement=True,
#             gaps=0.9,
#             mode=TrimmingMode.gappy,
#             use_log=False,
#         )
#         execute(**kwargs)

#         with open(
#             f"{here.parent}/expected/EOG091N44M8_aa.fa_gappy.complement", "r"
#         ) as expected:
#             expected_content = expected.read()

#         with open(complement_out_file, "r") as out_file:
#             output_content = out_file.read()

#         assert expected_content == output_content
