# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temperature = default_temp

        self.schedules={}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature  

    def __str__(self):
        lst=[]

        def_temp="Default temperature " + str(self.default_temperature) + " degrees"
        lst.append(def_temp)

        sorted=sorted(self.schedules)

        for i in sorted:
            temp=self.schedules[i]
            scheudle_line={i}+{temp} + " degrees"
            lst.append(scheudle_line)

        return '\n'.join(lst)
    
    # def get_target_temperature(time):




