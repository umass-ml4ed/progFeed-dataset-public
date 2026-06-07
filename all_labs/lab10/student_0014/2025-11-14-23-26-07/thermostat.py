# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat():
    def __init__ (self, default_temp = 68):
        self.default_temp = default_temp
        self.schedules = {}
    
    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__ (self):
        result =  f"Default temperature: {self.default_temp} degrees"
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n {temp} degrees"
        return result    
    
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        
        times = sorted(self.schedules)

        if query_time < times[0]:
            return  self.default_temp
        
        last_temp = self.default_temp
        for t in times:
            if query_time >= t:
                last_temp = self.schedules[t]
            else:
                break

        return last_temp


#dev = Thermostat(75)
#dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)

#print(Thermostat())