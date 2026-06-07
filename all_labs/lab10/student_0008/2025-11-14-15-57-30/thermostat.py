# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, dtemp=68):
        self.dtemp = dtemp
        self.sched = {}
    def add_schedule(self, time, temp):
        self.sched[time] = temp
    def __str__(self):
        x = f"Default temperature: {self.dtemp} degrees\n"
        sortSched = sorted(self.sched.items())
        for time, temp in sortSched:
            x += f"{time} {temp} degrees\n"
        return x.strip()
    def get_target_temperature(self, qtime):
        sortSched = sorted(self.sched.items())
        if qtime < sortSched[0][0]:
            return self.dtemp
        for i in range(len(sortSched)-1):
            time, temp = sortSched[i]
            if qtime <= time:
                return temp
        return sortSched[-1][1]