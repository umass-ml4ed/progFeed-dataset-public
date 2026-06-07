# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self._temperature = temp

        default_temp=68
        schedule={}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature  

    # def __str__():
        # return f'Temperature: {self._temperature}°F'
    
    # def get_target_temperature(time):




