# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat():
    def __init__(self, default=68):
        self.temp=default
        self.schedule={}

    def add_schedule(self, time, temperature):
        self.schedule[time]=temperature

    def __str__(self):
        x=(f'Default temperature {self.temp} degrees')
        schedule=sorted(self.schedule)
        for i in schedule:
            x+=(f'/n{i} {self.schedule[i]} degrees')
        return(x)
    
    def get_target_temperature(self, query_time):
        schedule=sorted(self.schedule)
        time=None
        for i in schedule:
            if i <= query_time:
                time=i
            else:
                break
        if time is None:
            return self.temp
        return self.schedule[time]