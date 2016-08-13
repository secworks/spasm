#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#=======================================================================
#
# spasm_cpu.py
# ------------
# This module contains the CPU class. The class is able to load
# a given cpu definition file and get the instruction set needed.
# The class can then be used to parse assembler source and
# generate code specific for the cpu.
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


#-------------------------------------------------------------------
# CPU()
#-------------------------------------------------------------------
class CPU:
    def __init__(self, verbose = False):
        self.verbose = verbose
        self.cpu_name = ""
        self.endianess = ""
        self.num_instructions = 0
        self.instruction_set = {}


    def load_cpu_definition(self, filename):
        with open(filename, 'rb') as source:
            for line in source:
                if self.verbose:
                    print(line)
                if "cpu_name" in line:
                    self.cpu_name = line.split(':')[1]
                    if self.verbose:
                        print("cpu_name: ", self.cpu_name)


#-------------------------------------------------------------------
# test_cpu()
#
# Loads a known cpu definition and print the resulting cpu.
#-------------------------------------------------------------------
def test_cpu():
    my_cpu = CPU(True)
    my_cpu.load_cpu_definition("cpu_defines/m6510_defines.txt")
    print(my_cpu)


#-------------------------------------------------------------------
# __name__
# Python thingy which allows the file to be run standalone as
# well as parsed from within a Python interpreter.
#-------------------------------------------------------------------
if __name__=="__main__":
    # Run the main function.
    sys.exit(test_cpu())

#=======================================================================
# EOF spasm_cpu.py
#=======================================================================
