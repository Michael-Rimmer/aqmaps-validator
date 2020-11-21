from constants import *

# Drone must move then read. Cannot read different sensor from same location.
class MoveThenReadValidator():

    def validate(flightValidator, flight, move, i):
        try:
            next_move = flight.flight_path[i+1].rstrip().split(',')
            if (move[1:-1] == next_move[1:-1]):
                print(f"Drone does not move between moves {i} and {i+1}\n")
                flight.valid = False
        except IndexError:
            pass
        except :
            flight.valid