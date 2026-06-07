# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED
import datetime
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}


    def add_schedule(self, time, temperature):
        self.schedules[time] = temperature

    def __str__(self):
        result = f"Default temperature: {self.default_temp} degrees"
        sorted_times = sorted(self.schedules)
        for time in sorted_times:
            temperature = self.schedules[time]
            result += f"\n{time} {temperature} degrees"
        return result

def get_target_temperature(query_time_str, schedules, default_temp):
    query_time = datetime.strptime(query_time_str, '%H:%M').time()
    if query_time >= datetime.strptime(schedules[-1]['time'], '%H:%M').time():
        return schedules[-1]['temperature']
    for i in range(len(schedules) - 1):
        time1 = datetime.strptime(schedules[i]['time'], '%H:%M').time()
        time2 = datetime.strptime(schedules[i+1]['time'], '%H:%M').time()
        if time1 <= query_time < time2:
            return schedules[i]['temperature']
    return default_temp


get_target_temperature('19:40')