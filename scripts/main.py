########################################
# IMPORTS
########################################

import meta_data as meta
import character_select as charsel

import os

########################################
# STATE
########################################

SN_START = 0
SN_CHARSEL = 1

class State:
    def __init__(self, state_name):
        self.state_name = state_name

    def at_state(self, state_name):
        return self.state_name == state_name

    def set_state(self, state_name):
        self.state_name = state_name

########################################
# OUTPUT
########################################

def _p(output):
    print(output, end='')

########################################
# STATE-BASED FUNCTIONS
########################################

def sn_start(state):
    _p(meta.NAME + " " + meta.VERSION_NAME + "\n\n")
    input("Press enter to continue...")

    state.set_state(SN_CHARSEL)

def sn_charsel(state):
    charlist = charsel.charlist()

    print("\033[1m\033[33m---Character Select---\033[0m\n")

    _p("\033[1m\033[34m")
    for i in range(len(charlist)):
        print(str(i+1) + ": " + charlist[i])

    print()
    _p("\033[35m")
    print(str(len(charlist)+1) + ": Create new character\033[0m\n")

    try:
        ans = int(input("Which do you choose? "))
    except ValueError:
        ans = 0

    if ans < 1 or ans > len(charlist)+1:
        print("\033[2J\033[1;1H\033[1m> \033[32mReally? You can't even do that? Try again.\033[0m\n")
        input("OK (Press enter)")
        return

    state.set_state(-1)

########################################
# START(MAIN)
########################################

def main():
    state = State(SN_START)
    _p("\033[2J\033[1;1H")

    while True:

        # App state checks
        if state.at_state(SN_START):
            sn_start(state)
            _p("\033[2J\033[1;1H")
            continue
        elif state.at_state(SN_CHARSEL):
            sn_charsel(state)
            _p("\033[2J\033[1;1H")
            continue
        else:
            break


if __name__ == "__main__":
    main()
