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
        count = 0
        for key in sort_schedule:
            if count <= len(sort_schedule):
                schedule_string = schedule_string + f"{key} {str(self.schedule[key])} degrees\n"
            else:
                schedule_string = schedule_string + f"{key} {str(self.schedule[key])} degrees"
        return f"Default temperature: {self.temp} degrees\n" + schedule_string
    def get_target_temperature(self, query_time):
        sort_schedule = sorted(self.schedule)
        for i in range(len(sort_schedule)):
            if query_time < sort_schedule[0]:
                return self.temp
            elif query_time < sort_schedule[i + 1]:
                return self.schedule[sort_schedule[i]]
            elif query_time > sort_schedule[-1]:
                return self.schedule[sort_schedule[-1]]


