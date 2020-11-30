from constants import *

# Drone must move then read. Cannot read different sensor from same location.
class MoveThenReadValidator():

    def validate(flightValidator, flight, move, i):
        try:
            next_move = flight.flight_path[i+1].rstrip().split(',')
            if (move[1] == next_move[1] and move[2] == next_move[2] and move[4] == next_move[4] and move[5] == next_move[5]):
                print(f"Drone does not move between moves {i} and {i+1}\n")
                flight.valid = False
        except IndexError:
            pass
        except :
            flight.valid