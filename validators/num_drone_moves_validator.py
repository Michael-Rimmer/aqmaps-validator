from constants import *

class NumDroneMovesValidator:

    def validate(flightValidator, flight, move, i):
        if i == 1:
            flight.num_moves = len(flight.flight_path)
            if flight.num_moves > MAX_DRONE_MOVES:
                flight.output += f"Max allowed drone moves = {MAX_DRONE_MOVES}. Flight has {len(flight.flight_path)}\n"
                flight.valid = False