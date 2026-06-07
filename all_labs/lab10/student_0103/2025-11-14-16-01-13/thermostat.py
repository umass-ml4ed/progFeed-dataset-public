# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, initX = 68):
        self.temperature = initX
        self.schedules = dict()
    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature
    def __str__(self):
        time_lst = sorted(self.schedules)
        stuff = ""
        for time in time_lst:
            stuff = stuff + f"{time} {self.schedules[time]} degrees\n"
        return f"Default temperature: {self.temperature} degrees\n{stuff}"
    def get_target_temperature(self, query_time):
        time_lst = sorted(self.schedules)
        selected = []
        for time in time_lst:
            if float(time[0]) > float(query_time[0]):
                continue
            elif float(time[0]) < float(query_time[0]):
                selected.append(time)
            elif float(time[0]) == float(query_time[0]):
                if float(time[1]) > float(query_time[1]):
                    continue
                elif float(time[1]) < float(query_time[1]):
                    selected.append(time)
                elif float(time[1]) == float(query_time[1]):
                    if float(time[3]) > float(query_time[3]):
                        continue
                    elif float(time[3]) < float(query_time[3]):
                        selected.append(time)
                    elif float(time[3]) == float(query_time[3]):
                        if float(time[4]) > float(query_time[4]):
                            continue
                        elif float(time[4]) <= float(query_time[4]):
                            selected.append(time)
        if len(selected) == 0:
            return self.temperature
        else:
            return self.schedules[sorted(selected)[-1]]

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)
print(dev.get_target_temperature('23:00'))