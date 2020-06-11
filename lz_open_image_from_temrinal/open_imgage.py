import argparse
import os
from PIL import Image

cwd = os.getcwd()

parser = argparse.ArgumentParser(description='--i "<image>"')
parser.add_argument("--i", default=None, help="when no image is specified as argument, the script will promt for image name")
parser.add_argument("--p", default=cwd, help="when no path is specified as argument, current working directly is used")
args = parser.parse_args()
image = i = args.i
p = args.p
os.chdir(p)

def show_image():
#    if not i:
#        image = input('Specify image to be opened: ')
    img = Image.open(image)
    img.show()

show_image()
