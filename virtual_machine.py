#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 13:27:18 2023

Creating a Virtual Machine in Python

@author: Meera Malhotra
"""

NUM_REG = 4  # number of registers
RAM_LEN = 256  # number of words in RAM

#OP codes to conduct different instructions
OPS = {
    "hlt": {"code": 0x1, "fmt": "--"},  # Halt program
    "ldc": {"code": 0x2, "fmt": "rv"},  # Load value
    "ldr": {"code": 0x3, "fmt": "rr"},  # Load register
    "cpy": {"code": 0x4, "fmt": "rr"},  # Copy register
    "str": {"code": 0x5, "fmt": "rr"},  # Store register
    "add": {"code": 0x6, "fmt": "rr"},  # Add
    "sub": {"code": 0x7, "fmt": "rr"},  # Subtract
    "beq": {"code": 0x8, "fmt": "rv"},  # Branch if equal
    "bne": {"code": 0x9, "fmt": "rv"},  # Branch if not equal
    "prr": {"code": 0xA, "fmt": "r-"},  # Print register
    "prm": {"code": 0xB, "fmt": "r-"},  # Print memory
}

OP_MASK = 0xFF  # select a single byte
OP_SHIFT = 8  # shift up by one byte
OP_WIDTH = 6  # op width in characters when printing

#instruction pointer, registers, and memory along with a prompt for output
class VirtualMachine:
    def __init__(self):
        self.initialize([])
        self.prompt = ">>"

    def initialize(self, program):
        assert len(program) <= RAM_LEN, "Program too long"
        self.ram = [
            program[i] if (i < len(program)) else 0
            for i in range(RAM_LEN)
        ]
        self.ip = 0
        self.reg = [0] * NUM_REG