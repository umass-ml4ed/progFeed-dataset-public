# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat: 
    def __init__(self, number=68): 
        self.default_temp = number
        self.schedules = {}

    def add_schedule(self, time: str, temperature: float): 
        self.schedules[time] = temperature
    
    def __str__(self):
        sorted_list = sorted(self.schedules)

        zoinks = f'Default Temperature: {self.default_temp} degrees'
        scoob = ''
        for whatever in sorted_list:
            scoob += f'\n{whatever} {self.schedules[whatever]} degrees'
        zoinks += scoob 

        return zoinks 
    
    def get_target_temperature(self, query_time):
        stupid_list = []

        for whatever in self.schedules: 
            if query_time >= whatever:
                stupid_list.append(whatever)
        
        a = max(stupid_list)

        if not stupid_list: 
            return self.default_temp
        else: 
            return self.schedules[a]


    
print(Thermostat())