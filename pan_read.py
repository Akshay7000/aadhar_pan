
import re


def pan_read_data(text):
    name = None
    fname = None
    dob = None
    pan = None
    nameline = []
    dobline = []
    panline = []
    text0 = []
    text1 = []
    text2 = []
    lines = text.split('\n')
    # print(text)
    for lin in lines:
        s = lin.strip()
        s = lin.replace('\n', '')
        s = s.rstrip()
        s = s.lstrip()
        text1.append(s)
    while ("" in text1):
        text1.remove("")

    text1 = list(filter(None, text1))
    lineno = 0
    for wordline in text1:
        xx = wordline.split('\n')
        if ([w for w in xx if re.search('(OMETAX|INCOMETAXDEPARWENT|INCOME|TAX|GOW|GOVT|GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT|PARTMENT|ARTMENT|INDIA|NDIA)$', w)]):
            text1 = list(text1)
            lineno = text1.index(wordline)
            break
    text0 = text1[lineno+1:]

    try:
        # Cleaning first names
        # print("finalPan", text0)
        # name = text0[0]
        # name = name.rstrip()
        # name = name.lstrip()
        # name = name.replace("8", "B")
        # name = name.replace("0", "D")
        # name = name.replace("6", "G")
        # name = name.replace("1", "I")
        # name = re.sub('[^a-zA-Z] +', ' ', name)
        # Cleaning Father's name
        lineno4 = 0
        for wordline4 in text0:
            xx4 = wordline4.split('\n')
            # print("wordline", xx4)
            if ([w4 for w4 in xx4 if re.search("(Name|ame|/Name)$", w4)]):
                text0 = list(text0)
                lineno4 = text0.index(wordline4)
                # print("wordline", lineno1)
                break
        name = text0[lineno4+1].replace("!", "I")
        name = name.replace("8", "S")
        name = name.replace("0", "O")
        name = name.replace("6", "G")
        name = name.replace("1", "I")
        name = name.replace("\"", "A")
        name = re.sub('[^a-zA-Z] +', ' ', name)
        # fname = text0[1]
        # fname = fname.rstrip()
        # fname = fname.lstrip()
        # fname = fname.replace("8", "S")
        # fname = fname.replace("0", "O")
        # fname = fname.replace("6", "G")
        # fname = fname.replace("1", "I")
        # fname = fname.replace("\"", "A")
        # fname = re.sub('[^a-zA-Z] +', ' ', fname)

        lineno3 = 0
        for wordline3 in text0:
            xx3 = wordline3.split('\n')
            # print("wordline", xx3)
            if ([w3 for w3 in xx3 if re.search("(Father's|Father's Name|Father)$", w3)]):
                text0 = list(text0)
                lineno3 = text0.index(wordline3)
                # print("wordline", lineno1)
                break
        fname = text0[lineno3+1].replace("!", "I")
        fname = fname.replace("8", "S")
        fname = fname.replace("0", "O")
        fname = fname.replace("6", "G")
        fname = fname.replace("1", "I")
        fname = fname.replace("\"", "A")
        fname = re.sub('[^a-zA-Z] +', ' ', fname)

        # Cleaning DOB
        # dob = text0[2][:10]
        # dob = dob.rstrip()
        # dob = dob.lstrip()
        # dob = dob.replace('l', '/')
        # dob = dob.replace('L', '/')
        # dob = dob.replace('I', '/')
        # dob = dob.replace('i', '/')
        # dob = dob.replace('|', '/')
        # dob = dob.replace('\"', '/1')
        # dob = dob.replace(" ", "")
        lineno2 = 0
        date_extract_pattern = "[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4}"
        for wordline2 in text0:
            xx2 = wordline2.split('\n')
            if ([w2 for w2 in xx2 if re.findall(date_extract_pattern, w2)]):
                text0 = list(text0)
                lineno2 = text0.index(wordline2)
                break
        dob = listToString(re.findall(date_extract_pattern, text0[lineno2]))
        # re.findall(date_extract_pattern, 'I\'m on vacation from 1/18/2021 till 1/29/2021')
        # Cleaning PAN Card details
        # text0 = findword(
        #     text1, '(Pormanam|Number|umber|Account|ccount|count|Permanent|ermanent|manent|wumm)$')
        # panline = text0[0]
        # pan = panline.rstrip()
        # pan = pan.lstrip()
        # pan = pan.replace(" ", "")
        # pan = pan.replace("\"", "")
        # pan = pan.replace(";", "")
        # pan = pan.replace("%", "L")

        lineno1 = 0
        for wordline1 in text0:
            xx1 = wordline1.split('\n')
            # print("wordline", xx1)
            if ([w1 for w1 in xx1 if re.search("(Card|Number|Permanent Account Number Card|Account|NUMBER|CARD|PER|ACCO)$", w1)]):
                text0 = list(text0)
                lineno1 = text0.index(wordline1)
                # print("wordline", lineno1)
                break
        pan = text0[lineno1+1]
    except:
        pass

    data = {}
    data['Name'] = name
    data['Father Name'] = fname
    data['Date of Birth'] = dob
    data['PAN'] = pan
    data['ID Type'] = "PAN"
    return data


def findword(textlist, wordstring):
    lineno = -1
    for wordline in textlist:
        xx = wordline.split()
        if ([w for w in xx if re.search(wordstring, w)]):
            lineno = textlist.index(wordline)
            textlist = textlist[lineno+1:]
            return textlist
    return textlist


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1
