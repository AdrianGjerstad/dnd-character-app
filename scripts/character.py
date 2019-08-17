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
        self.author = None
        self.name = name

        self._class_ = None
        self.level = None
        self.background = None
        self.race = None
        self.alignment = None
        self.experience_points = None

        self.strength = None
        self.dexterity = None
        self.constitution = None
        self.intelligence = None
        self.wisdom = None
        self.charisma = None

        self.inspiration = None
        self.proficiency_bonus = None

        self.saving_throw_strength = None
        self.saving_throw_dexterity = None
        self.saving_throw_constitution = None
        self.saving_throw_intelligence = None
        self.saving_throw_wisdom = None
        self.saving_throw_charisma = None

        self.acrobatics = None
        self.animal_handling = None
        self.arcana = None
        self.athletics = None
        self.deception = None
        self.history = None
        self.insight = None

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
            setattr(res, attr_name, tok)
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