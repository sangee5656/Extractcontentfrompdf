#to extract images from pdf file
#pip install PyMuPDF
#pip install pillow

import fitz #PyMuPDF
import PIL.Image  #pillow
import io

pdf = fitz.open("airtelbill.pdf")
counter = 1
for i in range(len(pdf)):
    page = pdf[i]
    images = page.get_images()
    for image in images:
        base_img = pdf.extract_image(image[0])
        image_data = base_img["image"]
        img = PIL.Image.open(io.BytesIO(image_data))
        extension = base_img["ext"]
        img.save(open(f"image{counter}.{extension}", "wb"))
        counter +=1
