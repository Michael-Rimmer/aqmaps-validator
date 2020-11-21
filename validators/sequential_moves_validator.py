from constants import *

class SequentialMovesValidator():

    def validate(flightValidator, flight, move, i):
        try:
            next_move = flight.flight_path[i+1].rstrip().split(',')
            if (move[3] != next_move[1] or move[4] != next_move[2]):
                print(f"Moves {i} and {i+1} not sequential. ([{move[3]},{move[4]}] != [{next_move[1]},{move[2]}])\n")
                flight.valid = False
        except IndexError:
            pass
        except :
            flight.valid