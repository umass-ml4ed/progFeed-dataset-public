class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        s = f'Default temperature: {self.default_temp} degrees'
        if self.schedules:
            lines = [f"{time} {self.schedules[time]} degrees" for time in sorted(self.schedules)]
            s += '\n' + '\n'.join(lines)
        return s

    def get_target_temperature(self, query_time):
        times = sorted(self.schedules)
        last_time = None
        for t in times:
            if t <= query_time:
                last_time = t
            else:
                break
        if last_time is None:
            return self.default_temp
        else:
            return self.schedules[last_time]
