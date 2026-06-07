# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def _init_(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}
        