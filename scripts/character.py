########################################
# IMPORTS
########################################

import os.path
from os import path

########################################
# CHARACTER
########################################

class Character:
    def __init__(self, name, error=None):
        self.error = error
        self.name_ = name

########################################
# SAVE CHARACTER
########################################



########################################
# LOAD CHARACTER
########################################

def parse_file(name, text):
    res = Character(name)

    tok = ""
    attr_name = None


    for c in text:
        if c == " ":
            attr_name = tok
            tok = ""
            continue
        elif c in "\r\n":
            setattr(res, attr_name, tok)
            tok = ""
        else:
            tok += c

    return res

def load_character(name):
    if path.exists('./' + name + '.char.dat'):
        data = open('./' + name + '.char.dat', 'rt').read().split('\n')[3:]
        return parse_file(name, data)
    else:
        return Character("", error="Character file not found: ./" + name + ".char.dat")