# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default_temp=68):
        """
        Constructor sets default temperature and initializes
        an empty schedule dictionary.
        """
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        """
        Stores or updates a time → temperature pair.
        """
        self.schedules[time] = temperature

    def __str__(self):
        """
        Returns a multi-line string showing:
        - default temperature
        - sorted schedule times and temperatures
        """
        result = f"Default temperature: {self.default_temp} degrees"

        if not self.schedules:
            return result

        for time in sorted(self.schedules):
            result += f"\n{time} {self.schedules[time]} degrees"

        return result

    def get_target_temperature(self, query_time):
        """
        Returns the target temperature at the given time.
        Rules:
        - Before first scheduled time → default temperature
        - Between schedule[i] and schedule[i+1] → temperature at schedule[i]
        - After last schedule → last schedule temperature
        """
        if not self.schedules:
            return self.default_temp

        times = sorted(self.schedules)

        if query_time < times[0]:
            return self.default_temp

        last_temp = self.default_temp
        for time in times:
            if time <= query_time:
                last_temp = self.schedules[time]
            else:
                break

        return last_temp
    
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev)