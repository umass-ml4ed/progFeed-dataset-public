# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, defaulttemp=68):
        self.defaulttemp = defaulttemp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        sol = f"Default temperature: {self.defaulttemp} degrees"

        for x in sorted(self.schedules):
            section = f"{x} {self.schedules[x]} degrees"
            sol += "\n" +section
        return sol
    
    def get_target_temperature(self, query):
        if not self.schedules:
            return self.defaulttemp
        time = sorted(self.schedules)

        if query < time[0]:
            return self.defaulttemp
        recent = time[0]
        for x in time:
            if x <= query:
                recent = x
            else:
                break
        return self.schedules[recent]

            