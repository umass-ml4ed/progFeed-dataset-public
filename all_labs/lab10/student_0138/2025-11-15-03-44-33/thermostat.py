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
        lines = []
        lines.append(f"Default temperature: {self.default_temp} degrees")
        for t in sorted(self.schedules):
            temp = self.schedules[t]
            lines.append(f"{t} {temp} degrees")
        return "\n".join(lines)

    
    def get_target_temperature(self, query_time):
        if not self.schedules:
            return self.default_temp
        times = sorted(self.schedules)
        last_time_before_or_equal = None
        for t in times:
            if t <= query_time:
                last_time_before_or_equal = t
            else:
                break
        if last_time_before_or_equal is None:
            return self.default_temp
        return self.schedules[last_time_before_or_equal]


if __name__ == "__main__":
    dev = Thermostat(75)
    dev.add_schedule('08:00', 60.4)
    dev.add_schedule('19:35', 75.5)
    dev.add_schedule('09:30', 58.2)
    dev.add_schedule('22:39', 68.2)

    print(dev)
    print(dev.get_target_temperature('23:00'))
    print(dev.get_target_temperature('16:35'))
    print(dev.get_target_temperature('05:55'))
    print(dev.get_target_temperature('08:00'))
    print(dev.get_target_temperature('12:00'))