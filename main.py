################################################################################
# CLI Enigma Machine Emulator - Main
# Created by Aiden Seay, Summer 2025

################################################################################
# Imports

from Utilities.constants import *
from Utilities.io import *
from Utilities.rotator import *
from Utilities.reflector import *

################################################################################
# Main Program

def main():

    # define machine configuration

    # define the rotors
    rotor_specs = ["III", "II", "I"]      # Right to left order
    rotor_ring_settings = [0, 0, 0]       # For each rotor
    rotor_positions = [0, 0, 0]           # Start at A for each

    rotors = []
    for spec, ring_setting, position in zip(rotor_specs, rotor_ring_settings, rotor_positions):
        wiring = ROTORS[spec]["wiring"]
        notch = ROTORS[spec]["turnover"]
        rotor = Rotor(wiring, notch, ring_setting, position)
        rotors.append(rotor)

    # define the reflector type
    reflector = Reflector(REFLECTORS["UKW-B"]["wiring"])

    # define the plug board
    plugboard = {
        # add up to 10 pairs as needed
    }

    def plugboard_swap(c):
        return plugboard.get(c, c)

    # define test string
    plaintext = "ILBDA CXMLV NXJTZ STSPZ FSQDD ZSBFR UUOZF PCJXY FBS"

    ciphertext = ""

    for char in plaintext:

        print(f"Rotor positions: {[r.rotor_position for r in rotors]}")

        # check if 
        if not char.isalpha():
            continue

        char = char.upper()

        # Step rotors before encoding
        step_rotors(rotors)

        # Plugboard in
        c = plugboard_swap(char)

        # Forward pass through rotors (right → left)
        for rotor in rotors:
            c = rotor.to_reflector(c)

        # Reflector
        c = reflector.reflect(c)

        # Backward pass through rotors (left → right)
        for rotor in reversed(rotors):
            c = rotor.from_reflector(c)

        # Plugboard out
        c = plugboard_swap(c)
        ciphertext += c

    # display result
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")

################################################################################

def step_rotors(rotors):
    right, middle, left = rotors

    # Double-stepping quirk:
    if middle.at_notch():
        middle.step()
        left.step()

    if right.at_notch():
        middle.step()

    right.step()

main()
################################################################################