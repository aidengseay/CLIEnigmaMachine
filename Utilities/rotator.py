################################################################################
# CLI Enigma Machine Emulator - Rotator Code
# Created by Aiden Seay, Summer 2025

################################################################################
# Imports
from Utilities.constants import *

################################################################################

class Rotor:
    
    """

    Description: This class represents a single Enigma rotor. This is one of 
    three rotators in the enigma machine. There are 5 different rotors.
    
    """

    def __init__(self, wiring, notch, ring_setting, rotor_position):

        """

        Description: Initializes a rotator object.

        Parameters:

            self
            wiring (str): The pattern of wiring that defines a kind of rotor 
                          (I-V)
            notch (str): The letter where the notch is at to turn the rotator
            ring_setting (int): The offset of the rotor's internal wiring (0-25)
                                changing the turnover index
            rotor_position (int): Determines where the rotor starts rotating 
                                  (0-25)

        Return None

        """

        # set variables to class attributes
        self.wiring = wiring
        self.notch = notch
        self.ring_setting = ring_setting
        self.rotor_position = rotor_position

        # calculate the turnover index from the ring setting
        self.turnover_index = ((ord(notch) - UNICODE_A - self.ring_setting)
                                                                  % NUM_LETTERS)
        
        # reverse the wiring diagram for return trip
        self.reverse_wiring = [''] * NUM_LETTERS
        for index, char in enumerate(wiring):
            self.reverse_wiring[ord(char) - UNICODE_A] = chr(index + UNICODE_A)


    def step(self):

        """
        
        Description: Steps the rotor forward by one position

        Parameters:

            self

        Return: None

        """

        self.rotor_position = (self.rotor_position + 1) % NUM_LETTERS


    def at_notch(self):

        """
        
        Description: Returns true if the rotor is at its turnover position

        Parameters:

            self

        Return (bool): true if at turnover position, false if not

        """

        return self.rotor_position == self.turnover_index
    

    def to_reflector(self, char):

        """
        
        Description: Manipulates character with the rotator going to the
                     the reflector

        Parameters:

            self
            char (str): The character that will be encoded

        Return: Encoded character

        """

        # convert letter to index
        input_index = ord(char.upper()) - UNICODE_A

        # convert pin the signal enters on the wiring wheel and get letter
        shifted_index = (input_index + self.rotor_position - self.ring_setting) % NUM_LETTERS
        wired_letter = self.wiring[shifted_index]

        # reverses pin conversion for next rotator and return letter
        output_index = (ord(wired_letter) - UNICODE_A - self.rotor_position + self.ring_setting) % NUM_LETTERS
        return chr(output_index + UNICODE_A)
    

    def from_reflector(self, char):

        """
        
        Description: Manipulates character with the rotator returning from the
                     reflector

        Parameters:

            self
            char (str): The character that will be encoded

        Return: Encoded character

        """

        # convert letter to index
        input_index = ord(char.upper()) - UNICODE_A

        # convert pin the signal enters on the wiring wheel and get letter
        shifted_index = (input_index + self.rotor_position - self.ring_setting) % NUM_LETTERS
        wired_letter = self.reverse_wiring[shifted_index]

        # reverses pin conversion for next rotator and return letter
        output_index = (ord(wired_letter) - UNICODE_A - self.rotor_position + self.ring_setting) % NUM_LETTERS
        return chr(output_index + UNICODE_A)
    
################################################################################