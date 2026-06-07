# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default=68):
        self.default = default
        self.schedule = {}

    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__(self):
        lines = [f"Default temperature: {self.default} degrees"]
        for x in sorted(self.schedule):
            lines.append(f"{x} {self.schedule[x]} degrees")
        return "\n".join(lines)
    
    def get_target_temperature(self,quary):
        for t in sorted(self.schedule, reverse=True):
            if t <= quary:
                return(self.schedule[t])
        return self.default
    

    




