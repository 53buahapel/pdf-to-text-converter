import pypdfium2 as pdfium
from PIL import Image
import pytesseract
import os
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("file", nargs='?', default=None)
parser.add_argument('-o', '--output', default='output.txt')
args = parser.parse_args().file
outfile = parser.parse_args().output

print('\n\033[36mpdf to text converter by kyruuu v0.1\033[32m\n')

if args == None:
    args = input('Enter the file name: ')
while True:
    try:
        pdf = pdfium.PdfDocument(args)
        break
    except:
        print('File not found')
        args = input('Enter the file name: ')

version = pdf.get_version() 
n_pages = len(pdf) 
string = ''
for i in tqdm(range(n_pages), desc='processing'):
    page = pdf[i]  
    bitmap = page.render(
        scale = 1,    
        rotation = 0,
    )
    pil_image = bitmap.to_pil()
    pil_image.save(f"{i}.png")
    image = Image.open(f'{i}.png')
    string += pytesseract.image_to_string(image)
    os.system(f'rm {i}.png')

print('\n\033[39mfile saved to', outfile)
open(outfile, 'w').write(string)