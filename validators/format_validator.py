from constants import *
import re

class FormatValidator:

    def validate(flightValidator, flight, move, i):
        move = ','.join(move)
        if not bool(re.match(DRONE_MOVE_FORMAT_REGEX, move)):
            flight.output += f"Line {i+1} does not match formatting expectations.\n"
            flight.valid = False