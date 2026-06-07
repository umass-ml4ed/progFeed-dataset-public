# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


class Thermostat:
    def __init__(self, number=68):
        self.default_temp = number
        self.schedules = {}
    
    def add_schedule(self,time:str, temperature:float):
        self.schedules[time] = temperature
    
    def __str__(self):
        lines = [f"Default temperature: {self.default_temp} degrees" ]
        
        for key,value in sorted(self.schedules.items()):
            
             lines.append(f"{key} {value} degrees")
        return '\n'.join(lines)
    def turn_to_mins(self,time):
        new_time = []
        new_time = time.split(":")
        return int(''.join(new_time))

    

    def get_target_temperature(self,target_time):
        final_temp = self.default_temp
        for time,temp in sorted(self.schedules.items()):
            if self.turn_to_mins(time) <= self.turn_to_mins(target_time):
                final_temp = temp
        return final_temp
            

    
        

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)


# print(dev.__str__())
print(dev.get_target_temperature('23:00')) 
print(dev.get_target_temperature('16:35') )
print(dev.get_target_temperature('05:55') )
print(dev.get_target_temperature('08:00') )
print(dev.get_target_temperature('12:00') )



