# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/9/6 15:23

import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)
if __name__ == '__main__':
    from atm.core import main

    main.identification()






