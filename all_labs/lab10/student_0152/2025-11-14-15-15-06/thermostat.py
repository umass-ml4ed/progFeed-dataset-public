# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.temps = {}
    def add_schedule(self, time, temp):
        self.temps[time] = temp
    def __str__(self):
        sort = [f'Default temperature: {self.temp} degrees']
        for time in sorted(self.temps): 
            sort.append(f'{time} {self.temps[time]} degrees')
        return '\n'.join(sort)
    def get_target_temperature(self, query):
        if not self.temps:
            return self.temp
        s = sorted(self.temps)
        if query < s[0]:
            return self.temp
        for time in s:
            if time <= query:
                s[0] = time
            else:
                break
        return self.temps[s[0]]