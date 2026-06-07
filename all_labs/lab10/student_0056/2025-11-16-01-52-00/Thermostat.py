# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED


class Thermostat:
    def __init__(self, defTemp = 68):
        self.default_temp = defTemp
        self.sceduled_temps = {}
    def add_schedule(self, t, temp):
        self.sceduled_temps[t] = temp
    def __str__(self):
        ans = f"Default Temperature: {self.default_temp} degrees"
        for t in sorted(self.sceduled_temps):
            ans += f"\n{t.strip()}{self.sceduled_temps[t]} degrees"
        return ans
    def get_target_temp(self, query_time):
        if not self.sceduled_temps:
            return self.default_temp
        
        times = sorted(self.sceduled_temps)
        
        if  query_time < times[0]:
            return self.default_temp
        latest= None
        for t in times:
            if t <= query_time:
                latest = t
            else:
                break
        if latest is not None:
            return self.sceduled_temps[latest]
        return self.default_temp      