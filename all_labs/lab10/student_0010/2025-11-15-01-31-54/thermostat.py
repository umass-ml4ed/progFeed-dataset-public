# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
        def __init__(self, temp = 68):
                self.temp = temp
                self.schedules = {}
        def add_schedule(self, time, temp):
                self.schedules[time] = temp
        def __str__(self):
                lines = [f"Default temperature: {self.temp} degrees"]
                sorted_times = sorted(self.schedules)
                for time in sorted_times:
                        temp = self.schedules[time]
                        lines.append(f"{time} {temp} degrees")
                return '/n'.join(lines)
        def get_target_temperature(self, time_target):
                target = None
                for time in self.schedules:
                        if time <= time_target:
                                if target is None or time > target: 
                                        target = time
                if target is None:
                        return self.temp
                else:
                        return self.schedules[target]
                


