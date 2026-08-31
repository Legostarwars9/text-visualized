from PIL import Image
from pathlib import Path
def read(path, verbose):
    image = Image.open(path).convert('RGB')
    output_path = Path.cwd() / "output.txt"
    number = 1
    while output_path.exists():
        output_path = Path.cwd() / f"output_{number}.txt"
        number += 1
    with open(output_path, "w", encoding="latin-1") as file:
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.getpixel((x, y))
                if verbose == True:
                    print(r, g, b)

                file.write(chr(r))
                file.write(chr(g))
                file.write(chr(b))
    print(f"Saved to {output_path}")