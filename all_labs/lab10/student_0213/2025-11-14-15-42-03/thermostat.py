# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:

    def __init__(self, temp=68):
        self.new_dict = {}
        self.new_dict[''] = temp

    def add_schedule(self, time, temp):
        self.dicty = {}
        self.dicty[time] = temp

my_thermostat = Thermostat()
my_thermostat.add_schedule('08:00', 60.4)