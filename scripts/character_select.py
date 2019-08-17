########################################
# IMPORTS
########################################

import os.path
from os import path

########################################
# FUNCTIONS
########################################

def charlist():
    if path.exists('./character_index.dat'):
        data = open('./character_index.dat', 'rt').read().split('\n')[3:]
        return data
    else:
        f = open('./character_index.dat', 'x')
        f = open('./character_index.dat', 'w+')

        f.write("DO NOT EDIT OR MOVE THIS FILE!\nThe program this file was created by only looks for this\nfile in this spot, also using a certain syntax. DO NOT CHANGE THIS.")
        f.close()

        return []

def removechar():
    if path.exists('./character_index.dat'):
        data = open('./character_index.dat', 'rt').read().split('\n')[3:]
    else:
        f = open('./character_index.dat', 'x')
        f = open('./character_index.dat', 'w+')

        f.write("DO NOT EDIT OR MOVE THIS FILE!\nThe program this file was created by only looks for this\nfile in this spot, also using a certain syntax. DO NOT CHANGE THIS.")
        f.close()
