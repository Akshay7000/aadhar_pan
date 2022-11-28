import re
import numpy as np


def read_Aadhar_Back(text):
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

    text1 = list(filter(None, text1))
    text0 = text1[:]

    print("->", lines)
    lineno1 = 0
    for wordline1 in text0:
        xx1 = wordline1.split('\n')
        # print("wordline", xx1)
        if ([w1 for w1 in xx1 if re.search("(Address|address|Address:|Address: C/O|c/o)$", w1)]):
            text0 = list(text0)
            lineno1 = text0.index(wordline1)

            break
    pan = text0[lineno1:1]
    print("pan---->>>", text0.remove(lineno1))

    # dob = listToString(re.findall(date_extract_pattern, text0[lineno1]))
    # arr = np.array(text0)
    # newarr = np.array_split(arr, lineno1-1)

    # main


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1


def splitArr(a, n, k):
    b = a[:k]
    return (a[k::]+b[::])
