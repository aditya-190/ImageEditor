#!/bin/usr/env python3
import os
from PIL import Image

total_images = 0

current_location = os.getcwd()
if not os.path.exists('Images'):
  os.mkdir('Images')

init_directory = str(input('Enter The Folder To Search For The Images: '))
end_directory = current_location + '\\Images'

init_format = str(input("Input the format you want me to convert From (example - .JPEG) : "))
end_format = str(input('Input the format you want me to convert To (example - PNG) : '))

for filename in os.listdir(init_directory):
  if(os.path.splitext(filename)[-1].upper() == init_format):
    im=Image.open(init_directory + "\\" + filename).rotate(45).resize((128,128)).convert('RGB').save((end_directory + '\\' + os.path.splitext(filename)[0].upper() + '.' + end_format),end_format)
    total_images += 1

print("Total {} Images Have Been Converted And Saved At: {}".format(total_images, end_directory))
