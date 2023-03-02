import pytest
from pathlib import Path

from Bio import (
    AlignIO,
    Phylo
)

from remarkit.info_content_calc import (
    calculate_desirabilities,
    create_info_content_matrices,
    calculate_information_content,
    calc_treeness,
    calc_rcv,
    calc_saturation
)


here = Path(__file__)

@pytest.fixture
def biopython_tree_object():
    return Phylo.read("tests/integration/samples/Acct.fa.treefile", "newick")

@pytest.fixture
def biopython_alignment_object():
    return AlignIO.read(open("tests/integration/samples/Acct.fa"), "fasta")

@pytest.fixture
def tree_path():
    return "tests/integration/samples/Acct.fa.treefile"

@pytest.fixture
def alignment_path():
    return "tests/integration/samples/Acct.fa"

@pytest.fixture
def input_contents():
    return [
        ["Acct", "tests/integration/samples/Acct.fa", "tests/integration/samples/Acct.fa.treefile"],
        ["Al12e", "tests/integration/samples/Al12e.fa", "tests/integration/samples/Al12e.fa.treefile"],
        ["Amcm", "tests/integration/samples/Amcm.fa", "tests/integration/samples/Amcm.fa.treefile"]
    ]

@pytest.fixture
def identifiers():
    return ["A", "B", "C", "D"]

@pytest.fixture
def treeness_over_rcv():
    return [4, 3, 2, 1]

@pytest.fixture
def saturation():
    return [4, 3, 2, 1]

@pytest.fixture
def treeness():
    return [4, 3, 2, 1]


class TestInfoContentCalc(object):
    def test_calculate_desirabilities(
            self,
            identifiers,
            treeness_over_rcv,
            saturation,
            treeness
    ):
        res = calculate_desirabilities(
            identifiers,
            treeness_over_rcv,
            saturation,
            treeness
        )

        expected = [
            ['A', 1.0, 1.0, 1.0, 1.0, 4, 4, 4],
            ['B', 0.666667, 0.666667, 0.666667, 0.666667, 3, 3, 3],
            ['C', 0.333333, 0.333333, 0.333333, 0.333333, 2, 2, 2],
            ['D', 0.0, 0.0, 0.0, 0.0, 1, 1, 1]
        ]

        assert res == expected

    def test_create_info_content_matrices(self, input_contents):
        
        identifiers, treeness_over_rcv, saturation, treeness = create_info_content_matrices(input_contents)

        expected_identifiers = ["Acct", "Al12e", "Amcm"] 
        expected_treeness_over_rcv = [0.6295, 1.114, 1.1704]
        expected_saturation = [0.0926, 0.6303, 0.1563]
        expected_treeness = [0.29, 0.3714, 0.2638]

        assert identifiers == expected_identifiers
        assert treeness_over_rcv == expected_treeness_over_rcv
        assert saturation == expected_saturation
        assert treeness == expected_treeness

    def test_calculate_information_content(self, alignment_path, tree_path):
        row = ["Acct", alignment_path, tree_path]

        res = calculate_information_content(row)

        assert res == [0.6295, 0.0926, 0.29]

    def test_calc_treeness(self, biopython_tree_object):
        res = calc_treeness(biopython_tree_object)

        assert res == 0.29

    def test_calc_rcv(self, biopython_alignment_object):
        res = calc_rcv(biopython_alignment_object)

        assert res == 0.4607

    def test_calc_saturation(self, biopython_alignment_object, biopython_tree_object):
        res = calc_saturation(biopython_alignment_object, biopython_tree_object)

        assert res == 0.0926
