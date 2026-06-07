# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedule= {}
    def add_schedule(self, time:str, temperature:float):
        self.schedule[time]=temperature

    def get_target_temperature(self, time: str):
        last_temp = self.default_temp
        sorted_times = sorted(self.schedule)

        for t in sorted_times:
            if t <= time:
                last_temp = self.schedule[t]
            else:
                break

        return last_temp


    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        sorted_times = sorted(self.schedule)

        if len(sorted_times) == 0:
            return result

        for time in sorted_times:
            temp = self.schedule[time]
            result += f"\n{time} {temp} degrees"

        return result


print(Thermostat())











