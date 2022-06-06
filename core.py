from cgi import test
import cv2
import pytesseract
from PIL import Image

#Open the file utilizing PIL
filename ='IMG_3892.PNG'
img1 = Image.open(filename)

#Get information about the image
width, height = img1.size
dim= [width, height]

tag1coord = [919,646,1172,724]
tag2coord = []

print(dim)

#Take out the necessary components of the image > the tags
#crop takes in left, top, right, bottom
#lower is less than upper, means coordinate system is based in top left 
#box size is 253 78 

tag1 = img1.crop(tag1coord)
tag1.show()
text1= pytesseract.image_to_string(tag1)
print(text1)
test
