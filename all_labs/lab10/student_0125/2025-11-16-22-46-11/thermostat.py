# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED
    
class Thermostat:
    def __init__(self, temperature=68):
        self.temperature = temperature
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.temperature} degrees"
        if self.schedules:
            for time in sorted(self.schedules):
                result += f"\n{time} {self.schedules[time]} degrees"
        return result

    def get_target_temperature(self, query_time):
        """
        Returns the target temperature for the given query_time.
        """
        if not self.schedules:
            return self.temperature
        sorted_times = sorted(self.schedules)

        for i, time in enumerate(sorted_times):
            if query_time < time:
                if i == 0:
                    return self.temperature
                else:
                    return self.schedules[sorted_times[i - 1]]

        return self.schedules[sorted_times[-1]]
    
from thermostat import Thermostat

t = Thermostat()
print(t)  # Should print default temperature: 68 degrees

t.add_schedule('08:00', 60.4)
print(t.get_target_temperature('08:00'))