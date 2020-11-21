import math
from constants import *

class FlightEndsNearDroneStartValidator():

    def validate(flightValidator, flight, move, i):
        try:
            if move[0] == len(flight.flight_path) :
                end_long = float(move[3])
                end_lat = float(move[4])

                distance = math.sqrt((DRONE_START[0]-end_long) ** 2 + (DRONE_START[1]-end_lat) ** 2)

                if distance >= CLOSE_TO_STARTING_POINT_DISTANCE:
                    flight.output += f"Drone flight ends too far from start location. {distance} >= {CLOSE_TO_STARTING_POINT_DISTANCE}\n"
                    flight.valid = False
        except:
            flight.valid = False