import math
from constants import *

class AngleValidator():

    def validate(flightValidator, flight, move, i):
        try:
            angle = move[3]
            if angle < 0 or angle > 350 or angle % 10 != 0:
                flight.output += f"Drone flight angle for move {move[0]} must be a multiple of 10 between 0-350 but it is: {angle}.\n"
                flight.valid = False
        except:
            flight.valid = False