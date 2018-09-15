from PIL import Image
import os
import time


def bright(source_name, box, brightness):
    source = Image.open(source_name)
    # print(source_name)
    #dest = 'new' + source_name.split('/static/init/')[1]
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
    source.paste(ic, eval(box))
    #source.save('./static/init/' + dest)
    source.save(source_name)
# box = '30, 30, 250, 250'
# bright('apple.1.jpg', box, 1.7)


# os.rename('./static/init/p1.jpeg', './static/init/' +
#           str(time.time()) + 'p1.jpeg')
