import cv2
import numpy as np
import os
import skimage.exposure
import math
import statistics
import argparse

def shadow_removea(img):
    '''
    removes shadows from the foreground of an image
    '''
    # TODO
    return img

def decode_segmap(source):
    '''
    identifies the background of an image and makes it transparent
    input:
        source (str) -- /path/to/image.jpg
    returns:
        result (array) -- a multidimensional array representation of the edited image
    '''
    # load image
    img = cv2.imread(source)
    
    #img = shadow_remove(img)

    # convert to gray
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # threshold
    thresh = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)[1]
    
    thresh = 255 - thresh
    
    # apply morphology to clean small spots
    unit = 2*(500//min(gray.shape))+1
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (unit,unit))

    morph = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_CLOSE, kernel)
    morph = cv2.morphologyEx(morph, cv2.MORPH_ERODE, kernel, borderType=cv2.BORDER_CONSTANT, borderValue=0)

    # blur dilate image
    blur = cv2.GaussianBlur(morph, (14-unit,14-unit), sigmaX=0, sigmaY=0, borderType = cv2.BORDER_DEFAULT)

    # stretch so that 255 -> 255 and 127.5 -> 0
    mask = skimage.exposure.rescale_intensity(blur, in_range=(127.5,255), out_range=(0,255))

    # put mask into alpha channel of input
    result = img.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:,:,3] = mask

    # Return a normalized output image for display
    return result

if __name__=='__main__':
    '''
    Run 'python3 jpg2png.py --dir /path/to/directory_containing_jpegs' to convert all jpegs in --dir to png with the background removed (i.e., transparent)
    '''
    parser = argparse.ArgumentParser(description='Convert jpg images to png, with the background removed')
    parser.add_argument('--dir', default=os.getcwd(), help='the directory where the jpg files are located')

    args = parser.parse_args()
    dir = args.dir

    if os.path.isdir(dir):
        for filename in os.listdir(dir):
            if filename.endswith(".jpg"):
                try:
                    res = decode_segmap(os.path.join(dir,filename))
                    cv2.imwrite('{}.png'.format(os.path.join(dir,filename)), res)
                    print("{} --> {}.png".format(filename, filename))
                except Exception as e:
                    print("Failed to convert {}: {}".format(filename, str(e)))
            else:
                continue
    else:
        raise ValueError('{} is NOT a directory'.format(dir))
