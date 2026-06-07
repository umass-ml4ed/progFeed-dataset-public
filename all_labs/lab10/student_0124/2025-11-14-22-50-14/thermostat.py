# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:

    def __init__(self, temp = 68):

        self.def_temp = int(temp)

        self.schedules = {}

    def add_schedule(self, time: str, temperature: float):

        self.schedules[time] = float(temperature)

    def __str__ (self):

        output = f"Default temperature: {self.def_temp} degrees\n"

        for key in sorted(self.schedules):

            output += f"{key} {self.schedules[key]} degrees\n"

        output = output.strip("\n")

        return output

    def get_target_temperature(self, q_time: str):

        self.requested_time = q_time

        for key in sorted(self.schedules, reverse = True):

            if self.requested_time >= key:

                return self.schedules[key]

        return self.def_temp
