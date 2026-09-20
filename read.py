from PIL import Image
from pathlib import Path
from time import *
import sys
def read(path, verbose=False, charset="latin-1"):
    path = Path(path)
    im = Image.open(path).convert("RGB")
    file = path.stem + path.suffix
    for infile in file:
         try:
             idk = True
         except OSError:
            pass
    if verbose == True:
        for infile in file:
            try:
                print(file, im.format, f"{im.size}x{im.mode}")
            except OSError:
                pass
    ltime = strftime(f"%m-%d_%H:%M:%S", localtime())
    txtfile = "output_text-" + ltime + ".txt"
    txt = open(txtfile, "x")
    txt.close()
    txt = open(txtfile, "a")
    pixel = im.getdata()
    for rgb in pixel:
        r, g, b = rgb
        txt.write(chr(r))
        txt.write(chr(g))
        txt.write(chr(b))
    txt.close()