########################################
# IMPORTS
########################################

import readline

import meta_data as meta
import character_select as charsel
import character as char

########################################
# VARIABLES
########################################

current_char = None

########################################
# STATE
########################################

SN_EXIT = -1
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
# INPUT
########################################

def _i(prompt=''):
    try:
        res = input(prompt)
    except KeyboardInterrupt:
        _p("\033[2J\033[1;1H")
        exit()

    readline.clear_history()

    return res

########################################
# STATE-BASED FUNCTIONS
########################################

def sn_start(state):
    _p(meta.NAME + " " + meta.VERSION_NAME + "\n\n")
    _i("Press enter to continue...")

    state.set_state(SN_CHARSEL)

def sn_charsel(state):
    charlist = charsel.charlist()

    print("\033[1m\033[33m---Character Select---\033[0m\n")

    _p("\033[1m\033[34m")
    for i in range(len(charlist)):
        print(str(i+1) + ": " + charlist[i])

    if len(charlist) > 0:
        print()

    _p("\033[35m")
    print(str(len(charlist)+1) + ": Create new character\033[0m\n")

    try:
        ans = int(_i("Which do you choose? "))
    except ValueError:
        ans = 0

    if ans < 1 or ans > len(charlist)+1:
        print("\033[2J\033[1;1H\033[1m> \033[32mReally? You can't even do that? Try again.\033[0m\n")
        _i("OK (Press enter)")
        return
    else:
        # Valid choice
        if ans < len(charlist)+1:
            # Existing character
            c = char.load_character(charlist[ans-1])
            if c.error:
                _p("\033[2J\033[1;1H\033[31m")
                print("Internal Error: " + c.error)
                print("In other words, the character \033[1m\033[4m" + charlist[ans-1] + "\033[0m\033[31m could not be found.\033[0m\n")
                print("\033[1m\033[34m(i) If you have a character file with that name, move it into the same folder as this program.\033[0m\n")
                print("\033[1m\033[34m(i) In the mean time, that entry will be deleted from the index of characters.\033[0m\n")
                _i("Press enter to try again...")
                return

            current_char = c

    #state.set_state(-1)

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
