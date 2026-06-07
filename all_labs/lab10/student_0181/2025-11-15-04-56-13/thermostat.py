# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature = 68):
        self.temp = temperature 
        self.schedule = {}

    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__(self):
        res = f"Default temperature: {self.temp} degrees"
        if self.schedule:
            for time in sorted(self.schedule):
                temp = self.schedule[time]
                res +=f"\n{time}{temp} degrees"

        return res 

    def get_target_temperature(self, query_time):
        if not self.schedule:
            return self.temp 
        
        sorted_time = sorted(self.schedule)

        if query_time < sorted_time[0]:
            return self.temp

        for i in range(len(sorted_times) - 1) :
            if sorted_time[i]<= query_time < sorted_time [i+1]:
                return self.schedule[sorted_time[i]]

        return self.schedule[sorted_time[-1]]






