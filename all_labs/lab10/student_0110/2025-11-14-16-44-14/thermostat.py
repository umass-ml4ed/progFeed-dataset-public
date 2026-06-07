# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


class Thermostat:
    def __init__(self, def_temp = 68):
        self.temp = def_temp
        self.schedule = {}
    def add_schedule(self, time = str, temperature = float):
        self.schedule[time] = temperature
    def __str__(self):
        sort_schedule = sorted(self.schedule)
        schedule_string = ""
        for key in sort_schedule:
            schedule_string = schedule_string + f"\n{key} {str(self.schedule[key])} degrees"
        return f"Default temperature: {self.temp} degrees" + schedule_string
    def get_target_temperature(self, query_time):
        sort_schedule = sorted(self.schedule)
        if len(sort_schedule) == 0:
            return self.temp
        for i in range(len(sort_schedule)):
            if str(query_time) < sort_schedule[0]:
                return self.temp
            elif str(query_time) >= sort_schedule[-1]:
                return self.schedule[sort_schedule[-1]]
            elif str(query_time) < sort_schedule[i + 1]:
                return self.schedule[sort_schedule[i]]
