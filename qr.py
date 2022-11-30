import cv2
from pyzbar.pyzbar import decode
from pyaadhaar.utils import isSecureQr
from pyaadhaar.decode import AadhaarSecureQr
from pyaadhaar.decode import AadhaarOldQr
import zlib


def qr_aadhar(url):

    img = cv2.imread(url)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    var = cv2.Laplacian(img, cv2.CV_64F).var()
    if var > 5:
        print("var ", var)
        code = decode(gray)

        if len(code) > 0:
            print("var ", code)
            received_qr_code_data = code[0].data
            isSecureQR = (isSecureQr(received_qr_code_data))
            if isSecureQR:
                print("isSecureQR main ghusa")
                secure_qr = AadhaarSecureQr(int(received_qr_code_data))
                decoded_secure_qr_data = secure_qr.decodeddata()
                print(decoded_secure_qr_data)
                return {"userData": decoded_secure_qr_data, "isOld": True}
            else:
                print("qrData", received_qr_code_data)
                obj = AadhaarOldQr(received_qr_code_data)
                obj = obj.decodeddata()
                if 'a' in obj:

                    return {"userData": obj, "isOld": True}
                else:

                    return {"userData": obj, "isOld": False}
        else:
            return {"userData": "", "isOld": False}

    else:
        print("oops..", var)
