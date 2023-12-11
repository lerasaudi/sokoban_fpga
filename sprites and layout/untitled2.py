#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 14:58:31 2023

@author: okhmakv
"""

translate_dict = {
    "#": "000",  # wall
    "!": "001",  # crate
    "@": "010",  # agent
    "-": "011",  # floor
    ",": "100",  # goal
    "=": "110"   # grey
#        "101"   # goal reached
}

# Open the file named "level.txt"
with open("level.txt", "r") as file:
    # Read each line in the file
    
    element_count = 0
    
    for line in file.readlines():
        # Iterate through each character in the line
        for char in line:
            # Check if the character is not a newline character
            if char != '\n':
                # Print the binary value corresponding to the character
                print(translate_dict[char], end=' ')
                
                # Increment the element count
                element_count += 1

# Print the total number of output elements
print("\nNumber of output elements:", element_count)
print(len("===================="))