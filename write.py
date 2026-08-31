from pathlib import Path
from PIL import Image
import math


def write(path):
    with open(path, "r", encoding="latin-1") as file:
        text = file.read()

    values = []

    # Convert characters into number values
    for character in text:
        values.append(ord(character))

    # Pad values until divisible by 3
    while len(values) % 3 != 0:
        values.append(0)

    # Convert every 3 values into one RGB pixel
    rgb_pixels = []

    for i in range(0, len(values), 3):
        rgb_pixels.append((
            values[i],
            values[i + 1],
            values[i + 2]
        ))

    # Calculate the smallest square that fits all pixels
    size = math.ceil(math.sqrt(len(rgb_pixels)))

    total_pixels = size * size

    # Add black pixels until the square is full
    while len(rgb_pixels) < total_pixels:
        rgb_pixels.append((0, 0, 0))

    # Create square image
    image = Image.new("RGB", (size, size))

    image.putdata(rgb_pixels)

    output_path = Path.cwd() / "output.png"

    image.save(output_path)

    print(f"Saved to: {output_path}")