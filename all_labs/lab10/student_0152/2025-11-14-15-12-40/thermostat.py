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
        sorted = sorted(self.temps)
        if not sorted:
            return self.temp
        if query < sorted[0]:
            return self.temp
        for time in sorted:
            if time <= query:
                sorted[0] = time
            else:
                break
        return self.temps[sorted[0]]