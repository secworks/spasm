# spasm #
Simple and Plug-in (or Pathetic) based Assembler.

## Introduction ##
(Everybody has written their own assembler, so why haven't I?)

This is a simple assembler primarily targeting the MOS 6502. The
main assembler is really agnostic when it comes to mnemonics and should
be possible to generate objects for any CPU with the correct CPU
plug-in. But at the moment it is more pathetic.

The assembler supports a set of commands prefixed as follows:
  Comments: "// comment". Rows beginning with comment prefix are ignored.
  Includes: ".include filename"
  Defines:  ".define screen = 0x0400"
  Scripts:  ".script filename"
  Data:     ".data 0x00, 0x10, 0x20, 0x40, 0xde, 0xad"
  Address:  ".addr 0x1000". Base for object generated.


## Implementation ##
Written in standard Python3 without any third party modules.


## Status ##

**(2016-07-15)**
A lot in my head, not much yet in the repo.
