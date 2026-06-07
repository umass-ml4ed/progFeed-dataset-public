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

        def_temp="Default temperature: " + str(self.default_temperature) + " degrees"
        lst.append(def_temp)

        sorted_times=sorted(self.schedules)

        for i in sorted_times:
            temp=self.schedules[i]
            scheudle_line=f"{i} {temp} degrees"
            lst.append(scheudle_line)

        return '\n'.join(lst)
    
    def get_target_temperature(self, time):
        if not self.schedules:
            return self.default_temperature
        sorted_times=sorted(self.schedules)
        latest_time=None
        for t in sorted_times:
            if t <= time:
                latest_time=t
            else:
                break
        if latest_time is not None:
            return self.schedules[latest_time]
        else:
            return self.default_temperature



