# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, dev=68):
        self.default_temp = dev
        self.schedules = {}
    def add_schedule(self, time: str, temp: float):
        self.schedules[time] = temp
    def  __str__(self):
        return f"Thermostat(desired_temp={self.default_temp}, schedules={self.schedules})"
    def get_target_temperature(self, query_time:str):
        if not self.schedules:
            return self.default_temp
        sorted_times = sorted(self.schedules.keys())
        if query_time < sorted_times[0]:
            return self.default_temp
        latest_time = None
        for t in sorted_times:
            if t <= query_time:
                latest_time = t
            else:
                break
        if latest_time is not None:
            return self.schedules[latest_time]
        return self.default_temp