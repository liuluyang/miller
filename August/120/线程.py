import os
import sys
from concurrent import futures


pp = ("CN IN US ID BR PK NG RU JP MX PH VN ET EG IR TR CD FR").split()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def save_flag(img, filename):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "wb") as fp:
        fp.write(img)


# def get_flag(cc):
#     url = "{}/{cc}/{cc}.gif".format("http://xx", cc=cc.lower())
#     res = requests.get(url)
#     return res.content


def show(text):
    print(text, end=" ")
    sys.stdout.flush()








