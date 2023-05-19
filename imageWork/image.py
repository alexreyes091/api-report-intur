import os
import io
from PIL import Image

PATH = b'C:\\main-report-pdf\\app-report-front\\src\\reports\\templates\\images'
PATH_IMAGE = b'\\src\\reports\\templates\\images\\'
def getPathImage():
    return PATH

def getNameFile(name, userId):
    return ((name.replace(" ", '')).encode('utf-8') + str(userId).encode('utf-8') + b'.png')


def getImageBytes(image_bytes, name, userId):
    """Get image from BytesIO object"""
    # image = Image.open(BytesIO(image_bytes))

    try:
        nameFile = getNameFile(name, userId)
        nameFilePath = (PATH_IMAGE + b'\\' + nameFile)
        pathFile = (PATH + b'\\' + nameFile)

        img = Image.open(io.BytesIO(image_bytes))

        if not os.path.exists(PATH):
            os.makedirs(PATH)
        
        with open(pathFile, "wb") as f:
            img.save(f, "PNG")
        
    except:
        print('Error: getImageBytes')
    
    return nameFilePath

   


