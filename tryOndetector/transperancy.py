from wand.image import Image
from wand.color import Color

with Image(filename="/home/hp/PycharmProjects/tryOn/images/t6.jpeg") as img:#select image from database
    img.format = 'png'
    with Color('#FDFDFD') as white:
        twenty_percent = int(65535 * 0.2)  # Note: percent must be calculated from Quantum
        img.transparent_color(white, alpha=0.0, fuzz=twenty_percent)
    #saving img here give database insert query
    img.save(filename="/home/hp/PycharmProjects/tryOn/images/result.png")
