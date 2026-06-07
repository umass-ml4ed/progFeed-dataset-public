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
        if not sorted(self.temps):
            return self.temp
        if query < sorted(self.temps)[0]:
            return self.temp
        for time in sorted(self.temps):
            if time <= query:
                sorted(self.temps)[0] = time
            else:
                break
        return self.temps[sorted(self.temps)[0]]