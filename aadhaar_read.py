import re


def adhaar_read_data(text):
    res = text.split()
    name = None
    dob = None
    adh = None
    sex = None
    nameline = []
    dobline = []
    text0 = []
    text1 = []
    text2 = []
    lines = text.split('\n')
    for lin in lines:
        s = lin.strip()
        s = lin.replace('\n', '')
        s = s.rstrip()
        s = s.lstrip()

        text1.append(s)

    print("listtostring", listToString(text1))
    if 'female' in text.lower():
        sex = "FEMALE"
    else:
        sex = "MALE"

    text1 = list(filter(None, text1))
    text0 = text1[:]

    try:

        # Cleaning first names
        name = text0[0]
        name = name.rstrip()
        name = name.lstrip()
        name = name.replace("8", "B")
        name = name.replace("0", "D")
        name = name.replace("6", "G")
        name = name.replace("1", "I")
        name = re.sub('[^a-zA-Z] +', ' ', name)

        # Cleaning DOB

        # dob = text0[1][-10:]
        # dob = dob.rstrip()
        # dob = dob.lstrip()
        # dob = dob.replace('l', '/')
        # dob = dob.replace('L', '/')
        # dob = dob.replace('I', '/')
        # dob = dob.replace('i', '/')
        # dob = dob.replace('|', '/')
        # dob = dob.replace('\"', '/1')
        # dob = dob.replace(":", "")
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

        # Cleaning Adhaar number details
        aadhar_number = ''
        for word in res:
            if len(word) == 4 and word.isdigit():
                aadhar_number = aadhar_number + word + ' '
        if len(aadhar_number) >= 14:
            print("Aadhar number is :" + aadhar_number)
        else:
            print("Aadhar number not read")
        adh = aadhar_number

    except:
        pass

    data = {}
    data['Name'] = name
    data['Date of Birth'] = dob
    data['Adhaar Number'] = adh
    data['Sex'] = sex
    data['ID Type'] = "Adhaar"
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
