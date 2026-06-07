# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat():
    def __init__(self, default_temp = 68, ):
        self.default_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, temperature):
        self.schedules[time] = float(temperature)

# dev = Thermostat(75)
# dev.add_schedule('08:00', 60.4)
# dev.add_schedule('19:35', 75.5)
# dev.add_schedule('09:30', 58.2)
# dev.add_schedule('22:39', 68.2)

    def __str__(self):
        if len(self.schedules) == 0:
            return (f"Default temperature: {self.default_temp} degrees")
        for time in sorted(self.schedules):
            default = (f"Default temperature: {self.default_temp} degrees")
            cases = f"\n{time} {self.schedules[time]} degrees"
        return default + cases
    def get_target_temperature(self, query_time):
        increasing_times = sorted(self.schedules)
        for time in increasing_times:
            if time <= query_time:
                largest_time = time
                return self.schedules[largest_time]
            if largest_time == None:
                return self.default_temp
            

# Default temperature: 75 degrees
# 08:00 60.4 degrees
# 09:30 58.2 degreesx
# 19:35 75.5 degrees
# 22:39 68.2 degrees





