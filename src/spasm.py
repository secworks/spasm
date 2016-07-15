#!/usr/bin/env python
# -*- coding: utf-8 -*-
#=======================================================================
#
# spasm.py
# --------
# An assembler for fun and no profit.
#
#
# Author: Joachim Strömbergson
# Copyright (c) 2016 Secworks Sweden AB
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in
#   the documentation and/or other materials provided with the
#   distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
#=======================================================================

#-------------------------------------------------------------------
# Python module imports.
#-------------------------------------------------------------------
import sys
import os
import argparse


#-------------------------------------------------------------------
# Defines.
#-------------------------------------------------------------------


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def assemble(source, dest, verbose=False):
    pass

#-------------------------------------------------------------------
# main()
#
# Parse arguments and call the real dpa functionality.
#-------------------------------------------------------------------
def main():
    __version__ = '0.01 alpha'

    parser = argparse.ArgumentParser(description = 'Parse input files to generate\
                                     object code for the specified architecture.')
    parser.add_argument("source", help = 'The source file.')
    parser.add_argument("dest", help = 'The destination file.')
    parser.add_argument('--verbose', action="store_true", default=False)
    parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    args = parser.parse_args()
    assmble(source, dest, verbose)


#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())

#=======================================================================
# EOF dpa.py
#=======================================================================
