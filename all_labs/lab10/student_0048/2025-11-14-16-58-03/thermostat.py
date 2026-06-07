# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.curr_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, newtemp):
        self.schedules[f'{time}'] = f'{newtemp}'
    def __str__(self):
        string = str()
        string +=(f"Default temperature: {self.curr_temp} degrees")
        for time in (sorted(self.schedules)):
                string += (f"\n{time} {self.schedules[time]} degrees")
        return string
    def get_target_temperature(self, time):
        erm =sorted(self.schedules, reverse = True)
        count = 0
        for i in erm:
            count += 1
            if count == (len(self.schedules)) and (i <= time) != True:
                return (self.curr_temp)
            elif i <= time:
                return (self.schedules[i])
                


        
        

    