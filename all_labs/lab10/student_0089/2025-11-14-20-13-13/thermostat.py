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
        new_str = "Default temperature: " + str(self.def_temp) + " degrees"
        if self.my_dict == {}:
            return new_str
        else:
            new_str = new_str + '\n'
            sorted_lst = sorted(self.my_dict)
            for i in sorted_lst:
                last_item = sorted_lst[-1] 
                if last_item != i:
                    new_str = new_str + i + " " + str(self.my_dict[i]) + " degrees" + "\n"
                else:
                    new_str = new_str + i + " " + str(self.my_dict[i]) + " degrees"
        return new_str
    
    def get_target_temperature(self, query_time):
        if self.my_dict == {}:
            return self.def_temp
        sorted_lst = sorted(self.my_dict)
        if query_time < sorted_lst[0]:
            return self.def_temp
        else:
            for i in range(0, len(sorted_lst) - 1):
                if query_time >= sorted_lst[i] and query_time < sorted_lst[i + 1]:
                    return sorted_lst[i]
            return sorted_lst[-1]
    

