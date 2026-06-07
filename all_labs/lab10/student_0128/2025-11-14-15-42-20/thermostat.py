# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__ (self, temp = 68):
        self.temp = temp
        self.schedule = {}
    
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def get_target_temperature(self, t_string):
        key_names = []
        for key in self.schedule:
            key_names.append(key)
        key_names.append(t_string)
        if len(set(key_names)) < len(key_names):
            return self.schedule[t_string]
        key_names = sorted(key_names)
        return self.schedule[key_names[key_names.index(t_string) - 1]]
    
    def __str__ (self):
        return_string = f'Default temperature: {self.temp} degrees\n'
        try:
            for key in sorted(self.schedule):
                return_string = return_string + f'{key} {self.schedule[key]} degrees\n'
        except KeyError:
            pass
        return_string = return_string[:-1]
        return return_string