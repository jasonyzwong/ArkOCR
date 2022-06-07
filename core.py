import cv2
import pytesseract
import easyocr
from PIL import Image

#############################################################
#This program extracts the tags from an Arknights screenshot
#and returns the possible combinations / 4* combos


#Definitions (absolute for now, relative once I figure out)
boxh = 78
boxw = 253
c1 = 917
c2 = 1216
c3 = 1515
r1 = 643
r2 = 773
reader = easyocr.Reader(['en'], )
tags = [None] * 5



#Open the file utilizing PIL, apply necessary OCR pre-processinge
filename ='IMG_3892.PNG'
img1 = Image.open(filename).convert("L")

img1 = cv2.imread(filename)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img2 = img1 



#Take out the necessary components of the image > the tags
#crop takes in left, top, right, bottom
#coordinate system is based in top left 
#box size is 253 78 
#square top left starting from first moving over is
#(917,643), (1216,643), (1515, 643), (920, 773), (1216, 773)
#todo > relative positions 

tag1 = img1[r1:r1+boxh, c1:c1+boxw]
tag2 = img1[r1:r1+boxh, c2:c2+boxw]
tag3 = img1[r1:r1+boxh, c3:c3+boxw]
tag4 = img1[r2:r2+boxh, c1:c1+boxw]
tag5 = img1[r2:r2+boxh, c2:c2+boxw]

tagimg =[tag1, tag2, tag3, tag4, tag5]

#testing iterating
for i in range(5):
    tags[i] = reader.readtext(tagimg[i], detail = 0, paragraph = True)[0]



print(tags)
