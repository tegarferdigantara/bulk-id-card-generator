import os
import random
from PIL import Image, ImageDraw, ImageFont

# Load the base image and create a drawing object
base_image = Image.new('RGBA', (303, 152), (255, 255, 255, 255))
draw = ImageDraw.Draw(base_image)

# Load the template image and paste it onto the base image
template_image = Image.open('template.png')
base_image.paste(template_image, (0, 0))

# Define font styles
font_name = ImageFont.truetype('font/OpenSans-SemiBold.ttf', size=12)
font_kota = ImageFont.truetype('font/OpenSans-SemiBold.ttf', size=12)

# Load name and city data
with open('nama.txt', 'r') as f:
    nama_data = f.read().splitlines()
with open('asal.txt', 'r') as f:
    kota_data = f.read().splitlines()
with open('list.txt', 'r') as f:
    foto = f.read().splitlines()

# Create the output folder if it does not exist
if not os.path.exists('output'):
    os.mkdir('output')

# Loop through each name and city pair
for i in range(len(nama_data)):
    # Choose a name and city
    nama = 'NAMA: ' + nama_data[i]
    kota = 'ASAL KOTA: ' + kota_data[i]

    # Load the photo and paste it onto the base image
    photo_path = os.path.join('foto', foto[i])
    photo = Image.open(photo_path)
    photo = photo.rotate(0)
    photo = photo.resize((85, 113), resample=Image.LANCZOS)
    base_image.paste(photo, (5, 22))

    # Draw Image 
    draw.rectangle((94, 66, 300, 84), fill=(255, 255, 255, 255)) #x1,y1,x2,y2 = x1 & x2 mean the widht of rectangle, y1 & y2 mean the height of rectangle
    draw.text((94, 66), kota, font=font_kota, fill='black') #x, y 
    
    draw.rectangle((94, 43, 300, 58), fill=(255, 255, 255, 255)) #x1,y1,x2,y2 = x1 & x2 mean the widht of rectangle, y1 & y2 mean the height of rectangle
    draw.text((94, 43), nama, font=font_name, fill='black') #x, y
    
    

    # Save the resulting image
    output_path = os.path.join('output', f'id_card_{i}.png')
    base_image.save(output_path)

