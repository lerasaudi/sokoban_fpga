#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:47:53 2023

@author: okhmakv
"""

# Input string of numbers
input_string = "110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 000 000 000 000 000 000 000 000 000 000 000 000 000 000 000 110 110 110 110 110 000 000 000 011 011 011 011 000 011 011 011 011 011 011 000 110 110 110 110 110 110 000 011 011 011 011 011 011 011 011 011 011 011 011 011 000 110 110 110 110 110 110 000 011 011 011 011 011 011 000 000 000 011 011 011 000 110 110 110 110 000 000 000 100 011 011 011 011 011 011 000 011 011 011 000 110 110 110 110 110 000 011 011 011 011 011 011 011 011 011 011 011 011 000 110 110 110 110 110 000 000 011 011 011 011 011 011 011 100 011 011 011 000 000 000 110 110 110 110 000 011 011 011 000 000 011 011 011 000 011 011 011 011 011 011 000 110 110 110 000 000 011 011 011 000 011 011 011 011 011 011 011 011 000 000 110 110 110 110 110 000 000 000 000 000 000 000 000 000 000 000 000 000 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110 110"

# Split the input string into a list of numbers
numbers = input_string.split()

# Convert each number to an integer
numbers = [str(num) for num in numbers]

print(numbers)


for number in range(len(numbers)):
    print(numbers[number],',')

colors = ['0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0001', '0010', '0010', '0010', '0010', '0001', '0000', '0000', '0010', '0001', '0010', '0010', '0001', '0010', '0000', '0000', '0010', '0010', '0011', '0001', '0010', '0010', '0000', '0000', '0010', '0010', '0001', '0001', '0010', '0010', '0000', '0000', '0010', '0001', '0010', '0010', '0001', '0010', '0000', '0000', '0001', '0010', '0010', '0010', '0010', '0001', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000']

numbers = [str(num) for num in colors]

print(numbers)


# Given sequence
four_bit_sequence = [
    '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000',
    '0001', '0010', '0010', '0010', '0010', '0001', '0000', '0000', '0010',
    '0001', '0010', '0010', '0001', '0010', '0000', '0000', '0010', '0010',
    '0011', '0001', '0010', '0010', '0000', '0000', '0010', '0010', '0001',
    '0001', '0010', '0010', '0000', '0000', '0010', '0001', '0010', '0010',
    '0001', '0010', '0000', '0000', '0001', '0010', '0010', '0010', '0010',
    '0001', '0000', '0000', '0000', '0000', '0000', '0000', '0000', '0000',
    '0000'
]

# Corresponding 12-bit representations
mapping_dict = {
    '0000': '001000111001',
    '0001': '100111011110',
    '0010': '010001101111',
    '0011': '111111111111'
}

# Convert each 4-bit value to its corresponding 12-bit representation
twelve_bit_values = [mapping_dict[four_bits] for four_bits in four_bit_sequence]

# Print the result
for twelve_bits in twelve_bit_values:
    print(twelve_bits + ',')
