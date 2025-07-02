################################################################################
# CLI Enigma Machine Emulator - Reflector Code
# Created by Aiden Seay, Summer 2025

################################################################################
# Imports
from Utilities.constants import *

################################################################################

class Reflector:

    """

    Description: This class represents a single Enigma reflector. This is one of 
    three rotators in the enigma machine. There are 2 different reflectors to
    choose from.
    
    """

    def __init__(self, wiring):

        """

        Description: Initializes a reflector object.

        Parameters:

            self
            wiring (str): The pattern of wiring that defines a kind of reflector 
                          (UKW-B or UKW-C)

        Return None

        """

        self.wiring = wiring


    def reflect(self, char):

        """

        Description: Completes a single substitution to go back through the
                     rotors

        Parameters:

            self
            char (str): The single character to get substituted for

        Return (str): character that is encoded

        """
        
        # does a single substitution to go back through the rotors
        index = ord(char.upper()) - UNICODE_A
        return self.wiring[index]
    
################################################################################