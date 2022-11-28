import cv2
from pyzbar.pyzbar import decode


from pyaadhaar.utils import isSecureQr
from pyaadhaar.decode import AadhaarSecureQr
from pyaadhaar.decode import AadhaarOldQr


def qr_aadhar(url):

    img = cv2.imread(url)
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    var = cv2.Laplacian(img, cv2.CV_64F).var()
    if var > 5:
        code = decode(gray)
        if len(code) > 0:
            qrData = code[0].data
            if isSecureQr(qrData):
                obj = AadhaarSecureQr(qrData)
                obj = obj.decodeddata()
                if 'a' in obj:
                    print("a")
                    return obj
                else:
                    print("b")
                    return obj
            else:
                obj = AadhaarOldQr(qrData)
                obj = obj.decodeddata()
                if 'a' in obj:

                    return {"userData": obj, "isOld": True}
                else:

                    return {"userData": obj, "isOld": False}
        else:
            return "error"

    else:
        print("oops..", var)
