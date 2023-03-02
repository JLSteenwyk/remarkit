import pytest
from argparse import Namespace
from remarkit.args_processing import process_args


@pytest.fixture
def args():
    kwargs = dict(
        input="tests/integration/samples/input_file_small.txt",
        output="tests/integration/samples/output",
        plot=False
    )
    return Namespace(**kwargs)


class TestArgsProcessing(object):
    def test_process_args_input_file_dne(self, args):
        args.input = "some/file/that/doesnt/exist"
        with pytest.raises(SystemExit):
            process_args(args)

    def test_process_args_in_equals_out(self, args):
        args.output = args.input
        with pytest.raises(SystemExit):
            process_args(args)

    def test_process_args_plot_default(self, args):
        res = process_args(args)
        assert res["plot"] == False

    def test_process_args_plot_svg(self, args):
        args.plot = "svg"
        res = process_args(args)
        assert res["plot"] is "svg"

    def test_process_args_plot_png(self, args):
        args.plot = "png"
        res = process_args(args)
        assert res["plot"] is "png"
