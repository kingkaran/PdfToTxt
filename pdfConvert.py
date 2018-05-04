#!/bin/pyhton3

import io
from PIL import Image
import pytesseract
from wand.image import Image as wndimg

pdf = wndimg(filename = "example.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imgBlob = []

for img in pdfImage.sequence:
	imgPage = wndimg(image = img)
	imgBlob.append(imgPage.make_blob('jpeg'))

result = []

for img in imgBlob:
	im = Image.open(io.BytesIO(img))
	text = pytesseract.image_to_string(im, lang='eng')
	result.append(text)

# for i in result:
# 	print(i.encode('utf-8'))

# print(result.encode('utf-8'))

with open('text.txt', mode='wb') as file:
	for i in result:
		file.write(i.encode('utf-8')) 
