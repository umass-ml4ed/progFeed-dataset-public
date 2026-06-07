# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temp = 68):
        self.curr_temp = default_temp
        self.schedules = {}
    def add_schedule(self, time, newtemp):
        self.schedules[f'{time}'] = f'{newtemp}'
    def __str__(self):
        string = str()
        string +=(f"Default temperature: {self.curr_temp} degrees\\n\n")
        count = 0
        for time in (sorted(self.schedules)):
            count += 1
            if count < len(self.schedules):
                string += (f"{time} {self.schedules[time]} degrees\n")
            else:
                string += (f"{time} {self.schedules[time]} degrees")
        return string
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)


    