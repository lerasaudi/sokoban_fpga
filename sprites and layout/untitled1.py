import numpy as np
from PIL import Image

def zoom_image(bitstream, original_width, original_height, zoom_factor):
    # Split the bitstream into 12-bit pixels
    pixels = [int(bitstream[i:i+12], 2) for i in range(0, len(bitstream), 12)]

    # Reshape the pixels into a 2D NumPy array (original_height, original_width)
    original_image = np.array(pixels).reshape((original_height, original_width))

    # Perform zooming
    zoomed_image = np.kron(original_image, np.ones((zoom_factor, zoom_factor)))

    # Convert back to 8-bit values (adjust this based on the actual bit-depth of your data)
    zoomed_image = (zoomed_image * 255 / np.max(zoomed_image)).astype(np.uint8)

    return zoomed_image

# Example usage
bitstream = "100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100111011110100100000011100100000011100100000011100100000011100111011110100111011110100111011110100100000011111101110000111101110000111101110000111101110000100100000011100111011110100100000011111101110000111101110000111101110000111101110000111101110000100101010100100100000011100100000011111101110000100101010100111101110000111101110000100101010100100101010100100100000011100100000011111101110000111101110000111101110000100101010100100101010100100101010100100100000011100111011110100100000011100100000011100100000011100100000011100100000011100100000011100111011110"

original_width = 8
original_height = 8
zoom_factor = 10

zoomed_image = zoom_image(bitstream, original_width, original_height, zoom_factor)

# Display the zoomed image
Image.fromarray(zoomed_image).show()