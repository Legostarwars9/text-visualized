from pathlib import Path
from PIL import Image
import math
from time import *


def write(path, verbose):
    path = Path(path)
    ltime = strftime(f"%m-%d_%H:%M:%S", localtime())
    imgfile = "output_image-" + ltime + ".png"
    txt = open(path, "r", encoding="latin-1")
    text = txt.read()
    leng = len(text)
    width = math.ceil(math.sqrt(leng/3))
    height = width
    image = Image.new("RGB" ,(width, height))
    numbers = text.encode("latin-1")
    num = list(numbers)
    a = 0
    img = image.load()
    for y in range(height):
        for x in range(width):
            r = num[a] if a < len(num) else 0
            g = num[a+1] if (a+1) < len(num) else 0
            b = num[a+2] if (a+2) < len(num) else 0
            a += 3
            if verbose:
                print(f"X:{x} Y:{y} - R:{r} G:{g} B:{b}")
            img[x, y] = (r, g, b)
    image.save(imgfile, "PNG")