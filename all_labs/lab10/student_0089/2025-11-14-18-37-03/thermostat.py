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
        if self.my_dict == {}:
            return new_str
        else:
            sorted_lst = sorted(self.my_dict)
        for i in sorted_lst:
            last_item = sorted_lst[-1] 
            if last_item != i:
                new_str = new_str + i + " " + str(self.my_dict[i]) + " degrees" + "\n"
            else:
                new_str = new_str + i + " " + str(self.my_dict[i]) + " degrees"
        return new_str
