# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        times = sorted(self.schedules)
        for t in times:
            result += f"\n{t} {self.schedules[t]} degrees"
        return result

    def get_target_temperature(self, query_time):
        if len(self.schedules) == 0:
            return self.default_temp
        times = sorted(self.schedules)
        if query_time < times[0]:
            return self.default_temp
        latest_time = None
        for t in times:
            if t <= query_time:
                latest_time = t
            else:
                break
        if latest_time is None:
            return self.default_temp

        return self.schedules[latest_time]

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
dev.get_target_temperature('23:00')  # → 68.2
dev.get_target_temperature('16:35')  # → 58.2
dev.get_target_temperature('05:55')  # → 75
dev.get_target_temperature('08:00')  # → 60.4
dev.get_target_temperature('12:00')  # → 58.2


print(dev)