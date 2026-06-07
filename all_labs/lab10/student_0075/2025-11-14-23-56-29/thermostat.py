# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temp = 68):
        self.temp = temp
        self.schedules = {}

    def __str__(self):
        lst = [f"Default Temperature: {self.temp} degrees"]

        for time in sorted(self.schedules):
            temp2 = self.schedules[time]
            lst.append(f"{time} {temp2} Degrees")

        return "\n".join(lst)
    
    def add_schedule(self, time, temp):
        self.schedule[time] = float(temp)

    def get_target_temperature(self, time):
        target_temp = self.temp
        for scheduled_time in sorted(self.schedules):
            if scheduled_time <= time:
                target_temp = self.schedules[scheduled_time]
            else:
                break
        return target_temp


dev = Thermostat(76)
dev.add_schedule(8.00, 56)


print(dev)


