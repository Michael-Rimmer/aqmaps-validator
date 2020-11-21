from constants import *

class FlightStartsAtDroneStartValidator():

    def validate(flightValidator, flight, move, i):
        try:
            if int(move[0]) == 1:
                start_long = float(move[1])
                start_lat = float(move[2])
                if start_long != DRONE_START[0] or start_lat != DRONE_START[1]:
                    flight.output += f"Drone move {move[0]} does not start at {DRONE_START}. Your flight starts at {start_long},{start_lat}\n"
                    flight.valid = False
        except:
            flight.valid = False