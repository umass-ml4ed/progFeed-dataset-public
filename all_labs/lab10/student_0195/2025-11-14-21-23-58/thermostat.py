# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temperature = 68):
        self.default_temperature = default_temperature
        self.schedule = {}
    
    def add_schedule(self, time, temp):
        self.schedule[time] = temp

    def __str__(self):
        sorted_sch = sorted(self.schedule)
        text = f"Default temperature: {self.default_temperature} degrees"
        for t in sorted_sch:
            temp = self.schedule[t]
            text += f"\n{t} {temp} degrees"
        return text
    
    def get_target_temperature(self, query_time):
        sorted_time = sorted(self.schedule.keys())
        target_temp = self.default_temperature
        for schedule_time in sorted_time:
            if schedule_time <= query_time:
                target_temp = self.schedule[schedule_time]
            else:
                break
        return target_temp