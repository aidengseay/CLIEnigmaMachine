################################################################################
# CLI Enigma Machine Emulator - Constants
# Created by Aiden Seay, Summer 2025

################################################################################
# Imports


################################################################################
# Constants

NUM_LETTERS = 26
UNICODE_A = 65

ENTRY_DISC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Rotator Disks (5 to choose from - pick 3)
ROTORS = {
    "I": {
        "wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "turnover": "Q", # notch is Y
    },
    "II": {
        "wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "turnover": "E", # notch is M
    },
    "III": {
        "wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "turnover": "V", # notch is D
    },
    "IV": {
        "wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB",
        "turnover": "J", # notch is R
    },
    "V": {
        "wiring": "VZBRGITYUPSDNHLXAWMJQOFECK",
        "turnover": "Z", # notch is H
    }
}

# Reflector (2 to choose from - pick 1)
REFLECTORS = {
    "UKW-B": {
        "wiring": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
    },
    "UKW-C": {
        "wiring": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
    }
}

# Keyboard Mechanism

# Input: Keyboard has 26 letters (A-Z)
# Output: Lampboard has 26 letters (A-Z) - same order as the Keyboard

# Plugboard
# makes every a -> b 
# can have up to 10 switches

# Steps
# Battery
# Keyswitch
# Plugboard
# Rotors
# Plugboard
# keyswitch 
# lightbulb
# battery

# once a key is pressed a rotor will turn
# first rotor rotates every key press
# second rotor rotates every 1/26 key press
# third rotor rotates when second rotator makes a full rotation

# Config Settings
# Rotor Order - Choose 3 of 5 and put in any order
# Ring Setting - shifting of the number wheels
# Rotor Starting Positions - set where the rotor starts
# Plugboard Connections - Up to 10 direct connections
