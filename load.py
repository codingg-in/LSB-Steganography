from PIL import Image
import sys

def load_image(image):
    try:
        image = Image.open(image)
    except IOError as e:
        print("Error accessing file : {}".format(e))
        sys.exit()
    return image
