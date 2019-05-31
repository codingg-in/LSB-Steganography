from PIL import Image, ImageFont
from PIL import ImageDraw
import textwrap
from load import load_image
from save import save_image
def convert_message_image(message, image_size):
    message_image = Image.new("RGB", image_size)
    font = ImageFont.truetype("times.ttf",15)
    drawer = ImageDraw.Draw(message_image)
    margin = 10
    offset = 10
    for line in textwrap.wrap(message, width = int(image_size[0]/10)):
        drawer.text((margin, offset), line, font = font)
        offset += 10

    return message_image
    



def encoder (input_file, output_file, message):
    image = load_image(input_file)
    red, green, blue = image.split()
    (width, height) = image.size

    message_image = convert_message_image(message, image.size)
    image_bw = message_image.convert('1')

    encoded_image = Image.new("RGB", (width, height))
    pix_val = encoded_image.load()
    for i in range(width):
        for j in range(height):
            red_pix = bin(red.getpixel((i, j)))
            message_pix = bin(image_bw.getpixel((i, j)))
            if message_pix[-1] == '1':
                red_pix = red_pix[:-1] + '1'
            else:
                red_pix = red_pix[:-1] + '0'
            pix_val[i, j] = (int(red_pix,2), green.getpixel((i, j)), blue.getpixel((i, j)))

    save_image(encoded_image, output_file)
