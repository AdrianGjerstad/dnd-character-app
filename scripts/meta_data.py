"""
This package contains every peice of meta data that is used with the Python app
called D&D Interactive Character Sheets.

The only thing created by this package is constants the conform to an upper case
constant name standard. Look at the source to determine what these are. For now,
all you need to know is that this works.
"""

########################################
# META CONSTANTS
########################################

# App Name
NAME = "D&D Interactive Character Sheets"

# App Version (SemVer)
VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0

# App Version Name (Displayable)
VERSION_NAME = str(VERSION_MAJOR) + "." + str(VERSION_MINOR) + "." + str(
    VERSION_PATCH
)
