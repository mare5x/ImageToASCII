import math
import argparse
import sys
from PIL import Image

# Table source: http://paulbourke.net/dataformats/asciiart/.
DARK_TO_LIGHT = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """

# Because fonts are usually taller than they are wide, we have to
# take that into account to maintain the desired image aspect ratio.
# Otherwise the image gets stretched out. 
FONT_WIDTH_HEIGHT_RATIO = 0.55

def prepare_image(path, width):
    """ Returns a PIL.Image.Image object ready to be converted. 
        
        width: output ASCII image width in characters.
    """

    # Convert to 8-bit grayscale. This avoids the need to care about colors,
    # since text is black and white anyways. Also resize the image, because
    # font size is more than 1 px. But we also have to stretch the image
    # to take the font width/height ratio into account.

    img = Image.open(path)
    img = img.convert(mode="L")
    height = img.height / img.width * width
    height = round(height * FONT_WIDTH_HEIGHT_RATIO)
    return img.resize((width, height))

def map_to_ascii(val, invert=False):
    val = 255 - val if invert else val
    x = val / 255  # 0 -> black, 255 -> white
    x = 1 - math.pow(math.cos(x * math.pi / 2), 3)  # Graph the function.
    idx = int(x * (len(DARK_TO_LIGHT) - 1))
    return DARK_TO_LIGHT[idx]

def img2ascii(path, width, invert=False, out=sys.stdout):
    img = prepare_image(path, width)
    for idx, val in enumerate(img.getdata()):
        print(map_to_ascii(val, invert=invert), end='', file=out)
        if idx % img.width == img.width - 1:
            print(file=out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=str, help="Image file path.")
    parser.add_argument("--dest", nargs='?', type=argparse.FileType('w'), default=sys.stdout,
        help="Output text file path. Leave empty to output to stdout.")
    parser.add_argument("--width", type=int, default=120, help="Output text width.")
    parser.add_argument("--invert", action="store_true", help="Invert black and white text.")
    parser.add_argument("--font_ratio", type=float, default=FONT_WIDTH_HEIGHT_RATIO, 
        help="Specify your font's width/height ratio, if the resulting image's aspect ratio is wrong.")
    args = parser.parse_args()
    FONT_WIDTH_HEIGHT_RATIO = args.font_ratio
    img2ascii(args.image, args.width, invert=args.invert, out=args.dest)