#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 23:40:10 2023

@author: okhmakv
"""

from PIL import Image
import os

def convert_to_coe(input_folder, output_folder, width, height):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith("01.png"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.coe")

            img = Image.open(input_file)
            img_resized = img.resize((width, height))
            img_gray = img_resized.convert('L')

            with open(output_file, 'w') as f:
                f.write("memory_initialization_radix=16;\n")
                f.write("memory_initialization_vector=\n")

                for y in range(height):
                    for x in range(width):
                        pixel_value = img_gray.getpixel((x, y))
                        f.write(f"{pixel_value:02X}")
                        if x < width - 1 or y < height - 1:
                            f.write(",\n ")
                        else:
                            f.write(";\n")

if __name__ == "__main__":
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Use the script directory as the input folder
    input_folder = os.path.join(script_directory)
    
    # Use the script directory as the output folder
    output_folder = os.path.join(script_directory, "converted_sprites")
    
    sprite_width = 8
    sprite_height = 8

    convert_to_coe(input_folder, output_folder, sprite_width, sprite_height)
