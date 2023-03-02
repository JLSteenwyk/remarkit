import pytest

from remarkit.parser import create_parser

@pytest.fixture
def parser():
    return create_parser()


class TestParser(object):
    def test_required_only(self, parser):
        input_path = 'my/input/file'

        parsed = parser.parse_args([input_path])

        assert parsed.input == input_path
        assert parsed.plot == None

    def test_plot_png(self, parser):
        input_path = 'my/input/file'
        parsed = parser.parse_args([input_path, '-p', 'png'])
        assert parsed.plot == 'png'

    def test_plot_svg(self, parser):
        input_path = 'my/input/file'
        parsed = parser.parse_args([input_path, '-p', 'svg'])
        assert parsed.plot == 'svg'

    def test_output(self, parser):
        output_path = 'my/output/file'
        parsed = parser.parse_args([output_path, '-o', 'svg'])
        assert parsed.input == output_path
