# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp: float = 68):
        self.default_temp = default_temp
        self.schedules: dict[str, float] = {}

    def add_schedule(self, time: str, temperature: float):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"
        return result

    def get_target_temperature(self, query_time: str):
        if not self.schedules:
            return self.default_temp

        sorted_times = sorted(self.schedules.keys())

        if query_time < sorted_times[0]:
            return self.default_temp

        for i in range(len(sorted_times) - 1, -1, -1):
            if query_time >= sorted_times[i]:
                return self.schedules[sorted_times[i]]
        return self.default_temp

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(Thermostat())
print(dev)
print(dev.get_target_temperature('23:00'))
print(dev.get_target_temperature('16:35'))
print(dev.get_target_temperature('05:55'))
print(dev.get_target_temperature('08:00'))
print(dev.get_target_temperature('12:00'))
