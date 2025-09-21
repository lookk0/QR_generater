#run this in terminal first: pip install qrcode[pil]
import qrcode
import os

folder = r"" #put folder path

link = input('put ur link: ')
filename = input('filename: ').strip() 
type = input('select kind of image (jpg / png): ').strip() 

img = qrcode.make(link)

filename = f"{filename}.{type}"
filepath = os.path.join(folder, filename)

img.save(filepath)
print(f"\tQR code saved at: {filepath}")