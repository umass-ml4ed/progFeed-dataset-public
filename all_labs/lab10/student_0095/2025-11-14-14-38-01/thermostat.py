# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}
    
    def add_schedule(self, time, temp):
        self.schedules[time] = temp
    
    def __str__(self):
        result = "Default temperature: " + str(self.default_temp) + " degrees"

        if len(self.schedules) == 0:
            return result

        sorted_times = sorted(self.schedules)

        for time in sorted_times:
            temp = self.schedules[time]
            result = result + "\n" + time + " " + str(temp) + " degrees"

        return result
    
    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            if query_time < time:
                index = sorted_times.index(time)
                if index == 0:
                    return self.default_temp
                else:
                    prev_time = sorted_times[index - 1]
                    return self.schedules[prev_time]
                
        last_time = sorted_times[-1]
        return self.schedules[last_time]
    

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev.get_target_temperature('23:00'))
print(dev.get_target_temperature('16:35'))
print(dev.get_target_temperature('05:55'))
print(dev.get_target_temperature('08:00'))
print(dev.get_target_temperature('12:00'))

print(Thermostat())
print(dev)