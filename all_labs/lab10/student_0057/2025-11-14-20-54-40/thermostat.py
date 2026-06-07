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

        if not self.schedules:
            return result

        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"

        return result

    def get_target_temperature(self, query_time):
        if not self.schedules:
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

if __name__ == "__main__":
    t1 = Thermostat()
    print("Test 1: Empty thermostat")
    print(t1)
    print()
    dev = Thermostat(75)
    dev.add_schedule('08:00', 60.4)
    dev.add_schedule('19:35', 75.5)
    dev.add_schedule('09:30', 58.2)
    dev.add_schedule('22:39', 68.2)

    print("Test 2: Thermostat with schedules")
    print(dev)
    print()

    print("Test 3: Temperature lookups")
    print("23:00 →", dev.get_target_temperature('23:00'))  # 68.2
    print("16:35 →", dev.get_target_temperature('16:35'))  # 58.2
    print("05:55 →", dev.get_target_temperature('05:55'))  # 75
    print("08:00 →", dev.get_target_temperature('08:00'))  # 60.4
    print("12:00 →", dev.get_target_temperature('12:00'))  # 58.2
