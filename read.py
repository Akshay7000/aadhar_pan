
import json
import pytesseract
import cv2
import numpy as np
import sys
import re
import os
from PIL import Image
import ftfy
import pan_read
import aadhaar_read
import aadhar_back
import io
from pan_aadhar_ocr import Pan_Info_Extractor, Aadhar_Info_Extractor, Aadhar_Extractor


def read_data(url):

    filename = url

    img = cv2.imread(filename)

    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    var = cv2.Laplacian(img, cv2.CV_64F).var()
    var = round(var, 2)
    if var < 5:
        print("Image is Too Blurry....")

        print(var)
        resp = {
            "msg": "Hard to read image Blur value must be > then 5, Image is Too Blurry....", "blurrValue": var}
        return resp
        # k = input('Press Enter to Exit.')
        # exit(1)
    else:
        text = pytesseract.image_to_string(Image.open(filename))
        print(var)
        # text_output = open('/Users/moreyeahs/Desktop/output.txt',
        #                    'w', encoding='utf-8')
        # text_output.write(text)
        # text_output.close()

        # file = open('/Users/moreyeahs/Desktop/output.txt', 'r', encoding='utf-8')
        # text = file.read()

        # text = ftfy.fix_text(text)
        # text = ftfy.fix_encoding(text)

        if "permanent" in text.lower() or "tax" in text.lower() or "department" in text.lower():
            data = pan_read.pan_read_data(text)
            # print(text)
            print("pan", data)
            return {"data": data, "text": text, "blurrValue": var}
        elif "male" in text.lower():
            data = aadhaar_read.adhaar_read_data(text)
            print("aadhaar_read", data)
            return {"data": data, "text": text, "blurrValue": var}
        elif "address:" in text.lower():
            extractor = Aadhar_Info_Extractor()
            add = extractor.find_address(filename)
            aadhar_back.read_Aadhar_Back(text)
            # print(add)
