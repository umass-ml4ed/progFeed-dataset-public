# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default=68):
        self.temperature=default
        self.schedules={}
    
    def add_schedule(self,time,temperature):
        self.schedules[time]=temperature
    
    def __str__(self):
        result= f'Default temperature: {self.temperature} degrees'
        if not self.schedules:
            return result

        result += "\n"
        lines=[f'{time} {self.schedules[time]} degrees'for time in sorted(self.schedules)]
        result+='\n'.join(lines)
        return result
    def get_target_temperature(self, query_time):
        
        if not self.schedules:
            return self.temperature

       
        sorted_times = sorted(self.schedules)

        
        if query_time < sorted_times[0]:
            return self.temperature

        last_time = sorted_times[0]  
        for time in sorted_times:
            if time <= query_time:
                last_time = time
            else:
                break  

        return self.schedules[last_time]

        


        
        



dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev.get_target_temperature('22:39'))