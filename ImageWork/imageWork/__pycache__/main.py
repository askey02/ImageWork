'''
Created on Jul 14, 2021

@author: keyas
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
import requests
from io import BytesIO

from image_functions import *

if __name__ == '__main__':
    # open an image file. The default path is where this python module is
    im = Image.open("SiriusAndViolet.jpg")
    print(im.width, im.height, im.mode, im.format)  # Display some info about the image