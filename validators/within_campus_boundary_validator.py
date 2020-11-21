from constants import *

class WithinCampusBoundaryValidator():

    def validate(flightValidator, flight, move, i):
        try:
            if (float(move[1]) >= CAMPUS_BOUNDARY_MAX_LONG 
              or float(move[3]) >= CAMPUS_BOUNDARY_MAX_LONG 
              or float(move[1]) <= CAMPUS_BOUNDARY_MIN_LONG 
              or float(move[3]) <= CAMPUS_BOUNDARY_MIN_LONG
              or float(move[2]) >= CAMPUS_BOUNDARY_MAX_LAT 
              or float(move[4]) >= CAMPUS_BOUNDARY_MAX_LAT
              or float(move[2]) <= CAMPUS_BOUNDARY_MIN_LAT
              or float(move[4]) <= CAMPUS_BOUNDARY_MIN_LAT):
                flight.output += f"Drone move {move[0]} travels outside campus boundary\n"
                flight.valid = False
        except:
            flight.valid = False