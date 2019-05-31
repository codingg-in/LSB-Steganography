from PIL import Image
from load import load_image
from save import save_image

def decoder(input_image, output_file):
    image = load_image(input_image)
    red = image.split()[0]
    width, height = image.size

    decoded_image = Image.new("RGB", (width, height))
    pix_val = decoded_image.load()

    for i in range(width):
        for j in range(height):
            if bin(red.getpixel((i, j)))[-1] == '0':
                pix_val[i, j] = (0, 0, 0)
            else:
                pix_val[i, j] = (255, 255, 255)
                
    save_image(decoded_image, output_file)
