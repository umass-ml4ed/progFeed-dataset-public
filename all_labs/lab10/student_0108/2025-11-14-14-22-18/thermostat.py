# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp=68):
        self._temperature = temp

        default_temp=68
        schedule={}

    def add_schedule(self, time, temperature):
        self.schedule[time]=temperature

            # If the time already exists, its value will be overwritten
            # by the new temperature; otherwise it will create a new entry

    #def __str__():
