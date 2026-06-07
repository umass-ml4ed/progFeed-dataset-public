# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}


    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            temperature = self.schedules[time]
            result += f"\n{time} {temperature} degrees"
        return result
    
    
    def get_target_temperature(self, query_time):
        times = sorted(self.schedules)
        if len(times) == 0:
            return self.default_temp
        if query_time < times[0]:
            return self.default_temp
        latest_time = times[0]
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break
        return self.schedules[latest_time]

    dev = Thermostat(75)       # ← dev is defined here
    dev.add_schedule('08:00', 60.4)
    dev.add_schedule('19:35', 75.5)
    dev.add_schedule('09:30', 58.2)
    dev.add_schedule('22:39', 68.2)