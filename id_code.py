# -- coding:utf-8 --

from PIL import Image
import os
import pytesseract
from pyocr import tesseract

#create a list stored the addresses of examples
gifList=[]

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s/%s' % (filepath, allDir))
        if "gif" in child:
            gifList.append(child)
eachFile("/Users/zhangmingxuan/Desktop/python_captcha/examples") #this is the folder to store some examples


#this is the way of shiyanlou to modify the gifs
for i in gifList:
    im = Image.open(i)
    im.convert("P")
    im2 = Image.new("P", im.size, 255)
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y, x))
            if pix == 220 or pix == 227:  # these are the numbers to get
                im2.putpixel((y, x), 0)
#save the modified gifs as convert.gif

    im2.save('convertpic/'+i[-10:])
#use tesseract
    code = pytesseract.image_to_string(im2)
    print '%s : %s' % (i[-10:], code)
