# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:53:25 2022

@author: Willem Roefs
"""

import sqlite3
import itertools
# %%
con = sqlite3.connect('Hyperwebster.db')
cur = con.cursor()
cur.execute("DELETE FROM HW")
# %%
# cur.execute('''CREATE TABLE HW (ABC)''')
length = 3
# ArrABC = []
ABC = [[' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
       'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']]

for com in itertools.product(*ABC, repeat=length):
    # print(combination)
    str1 = str('')
    for i in com:
        str1 += i
    # print(str1.split(' '))
    if len(str1.split(' ')) >= 2:
        print(len(str1.split(' ')))
    # cur.execute("select ABC from HW where ABC=?", (str1,))
    # data = cur.fetchall()
    # if not data:
    if com[-1] != ' ':
        if len(str1.split(' ')) == 1:
            cur.execute("INSERT INTO HW VALUES ('" + str1.strip() + "')")    
    # cur.execute("INSERT INTO HW VALUES ('" + str1 + "')")

# %%
con.commit()
con.close()