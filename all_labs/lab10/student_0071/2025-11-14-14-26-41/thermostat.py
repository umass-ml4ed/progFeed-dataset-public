# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, temperature=68):
        self.temperature = temperature
        self.schedule = {}
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature
    def __str__(self):
        result = f"Default temperature: {self.temperature} degrees\n"
        for time in sorted(self.schedule):
            result += f"{time} {self.schedule[time]} degrees\n"
        return result.rstrip('\n')
    def get_target_temperature(self, query_time:str) -> float:
        query_time = query_time.strip()
        target_temp = self.temperature
        for time, temperature in self.schedules:
            if query_time < time:
                break
            target_temp = temperature
        return target_temp
if __name__ == "__main__":
    dev = Thermostat(75)
    dev.add_schedule('08:00', 60.4)
    dev.add_schedule('09:30', 58.2)
    dev.add_schedule('19:35', 75.5)
    dev.add_schedule('22.39', 68.2)
