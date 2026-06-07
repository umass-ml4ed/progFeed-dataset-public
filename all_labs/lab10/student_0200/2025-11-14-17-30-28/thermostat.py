# Author    : REDACTED
# Email     : REDACTED
# Spire ID  : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp 
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = (f"Default temperature: {self.default_temp} degrees")
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += (f"\n{time} {temp} degrees")
        return result
    
    def get_target_temperature(self, query_time):
        sorted_times = sorted(self.schedules)
        if not sorted_times or query_time < sorted_times[0]:
            return self.default_temp
        target_temp = self.default_temp
        for time in sorted_times:
            if time <= query_time:
                target_temp = self.schedules[time]
            else:
                break
        return target_temp

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)      
print(dev)

dev.get_target_temperature('23:00') 
dev.get_target_temperature('16:35') 
dev.get_target_temperature('05:55') 
dev.get_target_temperature('08:00') 
dev.get_target_temperature('12:00') 
print(dev)

