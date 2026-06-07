# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, def_temp = 68):
        self.def_temp = def_temp
        self.my_dict = {}

    def add_schedule(self, time, temp):
        self.my_dict[time] = temp
    
    def __str__(self):
        new_str = ""
        new_str = new_str + "Default temperature: " + str(self.def_temp) + " degrees\n"
        if self.my_dict == {}:
            return new_str
        else:
            lst = sorted(self.my_dict)
