# Author: REDACTED
# Email: REDACTED
# SPIRE ID: REDACTED

class Thermostat:
    def __init__(self, deffytemp=68):
    
        self.default_temp = deffytemp
       
        self.scheds = {}

    def add_schedule(self, time, temperature):
        
        self.scheds[time] = temperature

    def __str__(self):
    
        text = "Default temperature: " + str(self.default_temp) + " degrees"

    
        for t in sorted(self.scheds):
            value = self.scheds[t]
            line = "\n" + t + " " + str(value) + " degrees"
            text += line

        return text

    def get_target_temperature(self, query_time):
        
        if len(self.schedules) == 0:
            return self.default_temp

        '''see if sorting can be done using fucntions?? method??'''
        times = sorted(self.scheds)

        
        if query_time < times[0]:
            return self.default_temp

        
        latest_time = times[0]
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break

        '''scheck if u did 2nd one correctly'''
        return self.scheds[latest_time]
