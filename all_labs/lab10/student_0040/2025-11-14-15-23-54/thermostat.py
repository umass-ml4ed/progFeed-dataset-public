# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self, default_temperature=68):
        self._default_temperature = default_temperature
        self._schedules = {}

    def __repr__(self):
        return f"Thermostat(default_temperature={self._default_temperature}, schedules={self._schedules})"
    
def add_schedule(self, time, temperature):
    self._schedules[time] = temperature

def __str__(self):
        output = f"Default temperature: {self._default_temperature} degrees"
        sorted_schedules = sorted(self._schedules.items())

        for i, (time, temp) in enumerate(sorted_schedules):
            output += f"\n{time} {temp} degrees"

        return output

def get_target_temperature(self, query_time):
        target_temp = self._default_temperature
        sorted_schedules = sorted(self._schedules.items())

        for time, temp in sorted_schedules:
            if time <= query_time:
                target_temp = temp
            else:
                break # Query time is before this schedule, so we found the latest applicable schedule
        return target_temp


from thermostat import Thermostat

print(Thermostat())
print("\n---")

thermostat1 = Thermostat()
print(thermostat1)

thermostat2 = Thermostat(75)
print(thermostat2)

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev)

dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(f"Test cases for get_target_temperature (default: {dev._default_temperature}, schedules: {dev._schedules}):")
print(f"Query time '23:00': {dev.get_target_temperature('23:00')} (Expected: 68.2)")
print(f"Query time '16:35': {dev.get_target_temperature('16:35')} (Expected: 58.2)")
print(f"Query time '05:55': {dev.get_target_temperature('05:55')} (Expected: 75)")
print(f"Query time '08:00': {dev.get_target_temperature('08:00')} (Expected: 60.4)")
print(f"Query time '12:00': {dev.get_target_temperature('12:00')} (Expected: 58.2)")