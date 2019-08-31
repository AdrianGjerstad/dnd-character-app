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
SN_CHARCREATE = 2

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
        elif ans == len(charlist)+1:
            # Create new
            state.set_state(SN_CHARCREATE)
            return

def sn_charcreate(state, inchar=None, last=0, author=None):
    character = inchar or char.Character(None)

    if last <= 0:
        author = _i("What is your name? ")
        if author is "":
            print("\033[2J\033[1;1H\033[1m> \033[32mUgh. C'mon, really?\033[0m\n")
            _i("OK (Press enter)")
            return char.Character(None), last, author

        last += 1

    _p("\033[2J\033[1;1H")

    if last <= 1:
        name = _i("What is your character's name? ")
        if name is not "":
            character.name_ = name
            character.author_ = author
        else:
            print("\033[2J\033[1;1H\033[1m> \033[32mUgh. C'mon, really?\033[0m\n")
            _i("OK (Press enter)")
            ch = char.Character(None)
            ch.author_ = author
            return ch, last, author

        last += 1

    _p("\033[2J\033[1;1H")

    if last <= 2:
        classes = ["Barbarian", "Bard", "Cleric"]

        for i in range(len(classes)):
            print("\033[1m\033[34m%i: %s\033[0m" % (i+1, classes[i]))

        ans = _i("\nPlease pick the class you would like: ")

        try:
            ans = int(ans)
        except ValueError:
            ans = 0

        if ans < 1 or ans > len(classes):
            print("\033[2J\033[1;1H\033[1m> \033[32mUgh. C'mon, really?\033[0m\n")
            _i("OK (Press enter)")
            return character, last, author

        character.class_ = classes[ans-1]

        last += 1

    if last <= 3:
        pass

    print(character)
    while True:
        pass
    state.set_state(-1)

########################################
# START(MAIN)
########################################

def main():
    state = State(SN_START)
    _p("\033[2J\033[1;1H")

    ch, last, auth = (char.Character(None), 0, None)
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
        elif state.at_state(SN_CHARCREATE):
            ch, last, auth = sn_charcreate(state, ch, last, auth)
            _p("\033[2J\033[1;1H")
            continue
        else:
            break


if __name__ == "__main__":
    main()
