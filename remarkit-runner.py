#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Convenience wrapper for running remarkit directly from source tree."""
import sys

from remarkit.remarkit import main

if __name__ == "__main__":
    main(sys.argv[1:])
