import sys

def save_image(image, output_file):
    try:
        image.save(output_file)
    except Exception as e:
        print("Image could not be written : {}".format(e))
        sys.exit()
