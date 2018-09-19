from PIL import Image
import os
import time


# @vectorize(["(char, float32[3], float32)"], target="cuda")
def colorChange(source_name, box, brightness):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b = ic.getpixel((x, y))

            red = int(r * brightness)
            red = min(255, max(0, red))

            green = int(g * brightness)
            green = min(255, max(0, green))

            blue = int(b * brightness)
            blue = min(255, max(0, blue))

            ic.putpixel((x, y), (red, green, blue))
            # print(ic)
            # print(eval(box))
    source.paste(ic, eval(box))
    source.save(source_name)


def colorChange_SVG(source_name, box, brightness):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b, a = ic.getpixel((x, y))

            red = int(r * brightness)
            red = min(255, max(0, red))

            green = int(g * brightness)
            green = min(255, max(0, green))

            blue = int(b * brightness)
            blue = min(255, max(0, blue))

            ic.putpixel((x, y), (red, green, blue))
            # print(ic)
            # print(eval(box))
    source.paste(ic, eval(box))
    source.save(source_name)


# @vectorize(["(char, float32[3])"], target="cuda")
def negative(source_name, box):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b = ic.getpixel((x, y))
            ic.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    source.paste(ic, eval(box))
    source.save(source_name)


def negative_SVG(source_name, box):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b, a = ic.getpixel((x, y))
            ic.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    source.paste(ic, eval(box))
    source.save(source_name)


# @vectorize(["(char, float32[3], float32)"], target="cuda")
# def white_black(source_name, box, brightness):
#     source = Image.open(source_name)
#     ic = source.crop(eval(box))
#     separator = 255 / brightness / 2 * 3
#     for x in range(ic.size[0]):
#         for y in range(ic.size[1]):
#             r, g, b = ic.getpixel((x, y))
#             total = r + g + b
#             if total > separator:
#                 ic.putpixel((x, y), (255, 255, 255))
#             else:
#                 ic.putpixel((x, y), (0, 0, 0))
#     source.paste(ic, eval(box))
#     source.save(source_name)


# def white_black_SVG(source_name, box, brightness):
#     source = Image.open(source_name)
#     ic = source.crop(eval(box))
#     separator = 255 / brightness / 2 * 3
#     for x in range(ic.size[0]):
#         for y in range(ic.size[1]):
#             r, g, b, a = ic.getpixel((x, y))
#             total = r + g + b
#             if total > separator:
#                 ic.putpixel((x, y), (255, 255, 255))
#             else:
#                 ic.putpixel((x, y), (0, 0, 0))
#     source.paste(ic, eval(box))
#     source.save(source_name)


# @vectorize(["(char, float32[3])"], target="cuda")
def gray_scale(source_name, box):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b = ic.getpixel((x, y))
            gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
            ic.putpixel((x, y), (gray, gray, gray))
    source.paste(ic, eval(box))
    source.save(source_name)


def gray_scale_SVG(source_name, box):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b, a = ic.getpixel((x, y))
            gray = int(r * 0.2126 + g * 0.7152 + b * 0.0722)
            ic.putpixel((x, y), (gray, gray, gray))
    source.paste(ic, eval(box))
    source.save(source_name)


# @vectorize(["(char, float32[3])"], target="cuda")
def sepia(source_name, box):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b = ic.getpixel((x, y))
            red = int(r * 0.393 + g * 0.769 + b * 0.189)
            green = int(r * 0.349 + g * 0.686 + b * 0.168)
            blue = int(r * 0.272 + g * 0.534 + b * 0.131)
            ic.putpixel((x, y), (red, green, blue))
    source.paste(ic, eval(box))
    source.save(source_name)


def sepia_SVG(source_name, box):
    source = Image.open(source_name)
    ic = source.crop(eval(box))
    for x in range(ic.size[0]):
        for y in range(ic.size[1]):
            r, g, b, a = ic.getpixel((x, y))
            red = int(r * 0.393 + g * 0.769 + b * 0.189)
            green = int(r * 0.349 + g * 0.686 + b * 0.168)
            blue = int(r * 0.272 + g * 0.534 + b * 0.131)
            ic.putpixel((x, y), (red, green, blue))
    source.paste(ic, eval(box))
    source.save(source_name)
