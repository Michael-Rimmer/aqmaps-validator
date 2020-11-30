from constants import *
import requests
import json
import math

class CloseToSensorValidator():

    def validate(flightValidator, flight, move, i):
        try:
            if (move[-1] != 'null'):
                words = move[-1].split('.')
                url = f"{HTTP_BASE_URL}/words/{words[0]}/{words[1]}/{words[2]}/details.json"
                details = json.loads(requests.get(url).content)
                sensor_coords = details['coordinates']
                distance = math.sqrt((float(move[4])-float(sensor_coords['lng'])) ** 2 + ((float(move[5])-float(sensor_coords['lat'])) ** 2))
                if distance >= DRONE_SENSOR_RANGE:
                    flight.output += f"Drone move {move[0]} is out of range of its sensor {'.'.join(words)}. Distance = {distance} but should be <  {DRONE_SENSOR_RANGE}\n"
                    flight.valid = False
        except:
            flight.valid = False