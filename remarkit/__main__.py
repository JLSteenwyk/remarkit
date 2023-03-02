"""remarkit.__main__: executed when remarkit is called as script"""
import sys

from .remarkit import main

main(sys.argv[1:])
