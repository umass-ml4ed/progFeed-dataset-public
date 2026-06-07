# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, def_temp=68):
        self.a = def_temp
        self.schedules1 = {}
    
    def add_schedule(self, time1, temp1):
        self.schedules1[time1] = temp1
    
    def __str__(self):
        first_line = f"Default temperature: {self.a} degrees" 
        sorted_schedule = sorted(self.schedules1)
        for time in sorted_schedule:
            first_line += f'\n {time} {self.schedules1[time]} degrees'
        return first_line
    
    def get_target_temperature(self, query_time):
        sorted_schedule = sorted(self.schedules1)
        temp_final = self.a
        for time in sorted_schedule:
            if time <= query_time:
                temp_final = self.schedules1[time]
        
        return temp_final

#dev = Thermostat(75)
#dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)
#print(dev)
        


