from collections import namedtuple
import argparse
import math
from PIL import Image


RGB = namedtuple("RGB", ['r', 'g', 'b'])

ASCII_TABLE = r' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'
TABLE_LEN = len(ASCII_TABLE)

color_bit_width = math.floor(math.log2(TABLE_LEN) / 3)


def rgb_to_int(rgb):
    width = math.pow(2, color_bit_width) - 1
    r = int(rgb.r / 255 * width)
    g = int(rgb.g / 255 * width)
    b = int(rgb.b / 255 * width)
    
    return (r << (color_bit_width * 2)) | (g << color_bit_width) | b


def rgb_to_ascii(rgb):
    return ASCII_TABLE[rgb_to_int(rgb)]


def convert_image(image_path, output_path, width, height):
    img = Image.open(image_path)
    img.thumbnail((width, height))
    with open(output_path, "w", encoding="utf-8") as output_file:
        col = 0
        for idx, rgb in enumerate(map(lambda x: RGB._make(x[:3]), img.getdata())):
            output_file.write(rgb_to_ascii(rgb))
            col += 1
            if (col >= img.width):
                col = 0
                output_file.write('\n')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    parser.add_argument("-o", "--outputpath", type=str, default="out.txt")
    parser.add_argument("-ww", "--width", type=int, default=128)
    parser.add_argument("-hh", "--height", type=int, default=128)
    args = parser.parse_args()

    convert_image(args.path, args.outputpath, args.width, args.height)
