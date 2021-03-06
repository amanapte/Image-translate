# Image text translator - see more in readme.
# Made by @TomasRoj in 2019 under MIT license.
# Imports all required components
from PIL import Image
import pytesseract
from googletrans import Translator
import os
import glob
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("src", help="Source language", type=str)
parser.add_argument("dst", help="Destination language", type=str)
args = parser.parse_args()



# Sets up the googletranslator api
translator = Translator()

# Edit this path to tesseract.exe on your system. On windows its by default in the following:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# Path to the images folder. Edit this to yours.
os.chdir("./test_images")
print("******************")
# Goes thru every image:
for images in glob.glob("*.jpg"):
    # Opens image
    im = Image.open(images)

    # Gets the image and translates it to Czech. You can specify own lang if you want.
    text = pytesseract.image_to_string(im, lang=args.src)
    text_translated = translator.translate(text, dest=args.dst)

    # Finally, print the translated image's text and print it.
    print(text_translated)
    print("\n")
    print("--------------------------------------------------")
    
# Again and again.
