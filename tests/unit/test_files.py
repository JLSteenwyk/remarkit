import imghdr
import os
from pathlib import Path

import pytest

from remarkit.files import (
    read_input_file,
    output_information_content,
    output_plot,
)

here = Path(__file__)

@pytest.fixture
def merged_df():
    return [
            ['Arpl24', 1.0, 1.0, 0.694804, 1.0, 1.2609, 0.5752, 0.418],
            ['Al12e', 0.8495790939922008, 0.808624, 0.771556, 0.779252, 1.114, 0.6303, 0.3714],
            ['Bpsma', 0.8171381378070046, 0.866076, 0.933696, 0.147797, 1.1581, 0.7467, 0.2381]
        ]

class TestAutomaticFileTypeDetermination(object):
    def test_read_input_file(self):
        # setup
        in_file = f"{here.parent}/examples/input_file_small.txt"

        # execution
        input_contents = read_input_file(in_file)

        # check results
        assert len(input_contents) == 20
        assert input_contents[0] == ["Acct", "tests/integration/samples/Acct.fa", "tests/integration/samples/Acct.fa.treefile"]

    def test_output_information_content(self, merged_df):

        output_information_content(merged_df, f"{here.parent}/examples/output")

        with open(
            f"{here.parent}/expected/test_output_info_content.txt", "r"
        ) as expected:
            expected_content = expected.read()

        with open(f"{here.parent}/examples/output.txt", "r") as out_file:
            output_content = out_file.read()

        assert expected_content == output_content

    def test_output_plot_png(self, merged_df):

        output_plot(merged_df, f"{here.parent}/examples/output", "png")

        assert os.path.isfile(f"{here.parent}/examples/output.png")
        assert imghdr.what(f"{here.parent}/examples/output.png") == "png"

    def test_output_plot_svg(self, merged_df):

        output_plot(merged_df, f"{here.parent}/examples/output", "svg")

        assert os.path.isfile(f"{here.parent}/examples/output.svg")
