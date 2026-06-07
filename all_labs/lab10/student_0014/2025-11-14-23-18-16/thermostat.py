# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat():
    def __init__ (self, default_temp = 68):
        self.default_temp = default_temp
        self.schedule = {}
    
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__ (self):
        result =  f"Default temperature: {self.default_temp} degrees"

        if len(self.schedule) == 0:
            return result
        
        for time in sorted(self.schedule):
            temp = self.schedule[time]
            result += f"\n {temp} degrees"
        return result    
    
    def get_target_temperature(self, query_time):
        if not self.schedule:
            return self.default_temp
        
        times = sorted(self.schedule)

        if query_time < times[0]:
            return  self.default_temp
        
        last_temp = self.default_temp
        for t in times:
            if query_time >= t:
                last_temp = self.schedule[t]
            else:
                break

        return last_temp


#dev = Thermostat(75)
#dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)

#print(Thermostat())