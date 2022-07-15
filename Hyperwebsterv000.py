# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:53:25 2022

@author: wimme
"""

import numpy as np
import scipy
import pandas as pd

Length = 6
ABC = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

totallines = (len(ABC)**Length)

wordlst = []

print(totallines)

lastword1 = np.full(Length, ABC[-1])
lastword = str()
for string in lastword1:
    lastword += string

print(lastword)
# while (latestword is not lastword):
#     lastestword = 
    
#     wordlist.append()