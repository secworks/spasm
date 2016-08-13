#!/usr/bin/env python3
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

from spasm_cpu import CPU


#-------------------------------------------------------------------
# Defines.
#-------------------------------------------------------------------
m6510_defines = "cpu_defines/m6510_defines.txt"


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def scan_source(source, verbose):
    linenum = 1
    lines = []

    if verbose:
        print("Scanning file %s" % source)

    with open(source) as src_file:
        for line in src_file:
            if not line.isspace() and not line[0:2] == "//":
                lines.append((linenum, line))
            linenum += 1

    if verbose:
        print("Number of source lines scanned: %d" % (linenum - 1))

    return lines



#-------------------------------------------------------------------
#-------------------------------------------------------------------
def load_opcode_db(opcode_source, verbose):
    linenum = 1
    lines = []
    opcodes = []

    if verbose:
        print("Loading opcodes from file %s" % opcode_source)

    with open(opcode_source) as opcode_file:
        for line in opcode_file:
            if not line.isspace() and not line[0:2] == "//":
                opcode_line = line.split()
                if opcode_line[3] == "//":
                    instruction = (opcode_line[0], "_", "_",
                                   opcode_line[1], opcode_line[2], opcode_line[3:])

                if opcode_line[4] == "//":
                    instruction = (opcode_line[0], opcode_line[1], "_",
                                   opcode_line[2], opcode_line[3], opcode_line[4:])

                if opcode_line[5] == "//":
                    instruction = (opcode_line[0], opcode_line[1], opcode_line[2],
                                   opcode_line[3], opcode_line[4], opcode_line[5:])

                opcodes.append(instruction)
            linenum += 1

    if verbose:
        print("Number of opcode source lines scanned: %d" % (linenum - 1))
        print("Number of opcodes loaded: %d" % len(opcodes))
    return opcodes


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def assemble(source, dest, verbose=False):
    my_cpu = CPU()

    opcode_db = load_opcode_db(m6510_defines, verbose)
#    source_lines = scan_source(source, verbose)
#    print source_lines


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
    parser.add_argument('-v', '--verbose', action="store_true", default=False)
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    args = parser.parse_args()

    if not os.path.isfile(args.source):
        print("Source file %s does not exist." % args.source)
        return(1)

    assemble(args.source, args.dest, args.verbose)


#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(main())

#=======================================================================
# EOF spasm.py
#=======================================================================
