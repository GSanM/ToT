"""
PDF TO TEXT CONVERTER

Gabriel S. Moraes
gsan.moraes@gmail.com

"""
from wand.image import Image
from PIL import Image as PI
import pyocr
import pyocr.builders
import io
import sys

def extractText(pdf, lang):
    #return list of extracted texts

    req_image = []
    final_text = []

    tool = pyocr.get_available_tools()[0]

    image_pdf = Image(filename=pdf, resolution=300)
    image_jpeg = image_pdf.convert('jpeg')

    for img in image_jpeg.sequence:
        img_page = Image(image=img)
        req_image.append(img_page.make_blob('jpeg'))

    for img in req_image: 
        txt = tool.image_to_string(
            PI.open(io.BytesIO(img)),
            lang=lang,
            builder=pyocr.builders.TextBuilder()
        )
        final_text.append(txt)
    
    return final_text

def createFile(name, text):
    #create file with extracted text

    file = open(name + ".txt", "w+")
    for page in text:
        file.write(page)
    file.close()

pdf = sys.argv[1]
name_ext = pdf.split('/')[-1]
name = name_ext.split('.')[0] #Corrigir caso hajam mais pontos

try:
    print("Extracting text...")
    text = extractText(pdf, sys.argv[2])
except:
    print("Error trying to extract the text.")
    print("Usage: python pdf_to_text.py <file.pdf> <language>")
    tool = pyocr.get_available_tools()[0]
    print("Avaliable languages %s. For more, see the tesseract available languages." % tool.get_available_languages())

try:
    print("Creating file...")
    createFile(name, text)
except:
    print("Error trying to create the file.")