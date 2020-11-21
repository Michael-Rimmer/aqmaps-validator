from flight import Flight

from validators.num_drone_moves_validator import NumDroneMovesValidator
from validators.format_validator import FormatValidator
from validators.flight_ends_near_drone_start_validator import FlightEndsNearDroneStartValidator
from validators.flight_starts_at_drone_start_validator import FlightStartsAtDroneStartValidator
from validators.move_length_validator import MoveLengthValidator
from validators.within_campus_boundary_validator import WithinCampusBoundaryValidator
from validators.close_to_sensor_validator import CloseToSensorValidator
from validators.sequential_moves_validator import SequentialMovesValidator
from validators.move_then_read_validator import MoveThenReadValidator

# Third party
import glob
import math

class FlightValidator():

    def __init__(self, flights):
        self.flights = flights
        self.output = ""
        
        self.validators = []
        self.validators.append(NumDroneMovesValidator)
        self.validators.append(FormatValidator)
        self.validators.append(FlightEndsNearDroneStartValidator)
        self.validators.append(FlightStartsAtDroneStartValidator)
        self.validators.append(MoveLengthValidator)
        self.validators.append(WithinCampusBoundaryValidator)
        self.validators.append(CloseToSensorValidator)
        self.validators.append(SequentialMovesValidator)
        self.validators.append(MoveThenReadValidator)

    def validate(self):

        print(f"Validating {len(self.flights)} flights...\n")
        self.output = ""
        
        # Iterate over each flight
        for flight_file, flight in self.flights.items():

            print(flight_file)

            # Iterate over each move in flight
            for i,move in enumerate(flight.flight_path):
                move = move.rstrip().split(',')
                
                # Iterate over each validator
                for validator in self.validators:
                    validator.validate(self, flight, move, i)
    
        self.print_output()

    def print_output(self):

        num_valid = 0

        for flight_file, flight in self.flights.items():
            
            if flight.valid:
                num_valid +=1 
            else:
                self.output += f"---------------------\n"
                self.output += f"{flight_file}\n"
                self.output += flight.output
                self.output += f"---------------------\n"


        self.output += f"{num_valid}/{len(self.flights)} flights successful"
        print(self.output)
        return self.output


    def output_to_file(self, filename):
        with open(filename, 'w') as outfile:
            outfile.write(self.print_output())

if __name__ == '__main__':

    flights = {}

    # Iterate over all flight path files
    for flight_file in glob.glob('flightpaths/flightpath*.txt'):

        with open(flight_file, 'r') as flight_path:
            flights[flight_file] = Flight(flight_path.readlines())

    flight_validator = FlightValidator(flights)
    flight_validator.validate()