########################################
# IMPORTS
########################################

import os.path
from os import path

from types import *

########################################
# CHARACTER
########################################

class Character:
    def __init__(self, name, error=None):
        self.error = error

        self.author_ = None
        self.name_ = name

        self.class_ = None
        self.level_ = None

        self.background_ = None
        self.alignment_ = None

        self.race_ = None
        self.xp_ = None

        self.strength = Modifier()

    def __repr__(self):
        result  = f'{self.name_} ({self.author_}\'s Character)\n'
        result += f'Class: {self.class_}'

        return result

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
    ignore_line = False

    for c in text:
        if c == "#" and attr_name is None and not ignore_line:
            ignore_line = True
        elif c == "-" and attr_name is None and not ignore_line:
            attr_name = tok
            tok = ""
            continue
        elif c in "\r\n" and (attr_name is not None and tok != "") and not ignore_line:
            setattr(res, attr_name + "_", tok)
            tok = ""
            attr_name = None
            continue
        elif not ignore_line:
            tok += c
            continue
        elif c in "\r\n" and ignore_line:
            ignore_line = False
            tok = ""
            attr_name = None
            continue

    return res

def load_character(name):
    if path.exists('./' + name + '.char.dat'):
        data = open('./' + name + '.char.dat', 'rt').read().split('\n')[3:]
        return parse_file(name, data)
    else:
        return Character("", error="Character file not found: ./" + name + ".char.dat")