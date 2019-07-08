"""
PDF TO IMAGE CONVERTER

Gabriel S. Moraes
gsan.moraes@gmail.com

"""
from wand.image import Image
import os
from pathlib import Path
import sys

def convertPDF(nome):
    #convert pdf pages to images

    file_dir = Path("./" + nome)

    if not file_dir.is_dir():
        os.system("mkdir " + nome)

    with(Image(filename=nome + ".pdf", resolution=300)) as source: 
        images = source.sequence
        pages = len(images)
        for i in range(pages):
            n = i + 1
            newfilename = "./" + nome + "/" + str(n) + '.jpeg'
            page_file = Path(newfilename)
            if not page_file.is_file():
                Image(images[i]).save(filename=newfilename)

pdf = sys.argv[1]
nome_ext = pdf.split('/')[-1]
nome = nome_ext.split('.')[0]

try:
    convertPDF(nome)
except:
    print("Error trying to convert.")
    print("Usage: python pdf_to_image.py <file.pdf>")