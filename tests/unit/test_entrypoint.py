# import os
# import subprocess


# class TestEntrypoint(object):
#     def test_help(self):
#         cmd = "remarkit --help"
#         exit_status = os.system(cmd)
#         assert exit_status == 0

#     def test_run(self):
#         cmd = "remarkit tests/integration/samples/input_file_small.txt"
#         exit_status = os.system(cmd)
#         assert exit_status == 0

#     def test_input_error(self):
#         cmd = "remarkit /file/doesnt/exist"
#         response = subprocess.check_output([cmd], stderr=subprocess.STDOUT, shell=True)
#         assert response == b"Input file does not exist\n"

#     def test_run_no_args(self):
#         cmd = "remarkit"
#         exit_status = os.system(cmd)
#         assert exit_status == 0
