# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, initial_temp=68):
        self.temperature = initial_temp

    def add_schedule(self, time, temperature):
        self.scedules[time] = float(temperature)

    def __str__(self):
        lines = []
        lines.append(f"Default Temperature: {self.temperature}°F")

        for time in sorted(self.scedules):
            temp = self.scedules[time]
            lines.append(f"At {time}, set to {temp}°F")
        return "\n".join(lines)
    
    def get_target_temperature(self, query_time):
        if not self.scedules:
            return self.temperature
        times = sorted(self.scedules)
        if query_time < times[0]:
            return self.temperature
        
        last_times = times[0]
        for time in times:
            if time <= query_time:
                last_times = time
            else:
                break
        return self.scedules[last_times]