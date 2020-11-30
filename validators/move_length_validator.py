import math
from constants import *

class MoveLengthValidator():

    def validate(flightValidator, flight, move, i):
        try:
            start_long = float(move[1])
            start_lat = float(move[2])
            end_long = float(move[4])
            end_lat = float(move[5])

            distance = math.sqrt((start_long-end_long) ** 2 + (start_lat-end_lat) ** 2)

            # SEE ILP PIAZZA @292
            # Rounding errors should not give rise to an error of much more than 1e-14 in the length of the drone move.
            if not math.isclose(distance, DRONE_MOVE_LENGTH, abs_tol=0.00000000000001):
                flight.output += f"Drone move {move[0]} has length {distance} but should be {DRONE_MOVE_LENGTH}\n"
                flight.valid = False
        except:
            flight.valid = False