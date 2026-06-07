# Author: REDACTED
# Email: REDACTED
# Spire ID: REDACTED

class Thermostat:
    def __init__(self,d_temp=68):
        self.d_temp = d_temp
        self.schedule = {}  

    def add_schedule(self,time,temp):
        self.schedule[time] = float(temp)

    def __str__(self):
        res = f"Default temperature: {self.d_temp} degrees"

        if len(self.schedule) == 0:
            return res

        sorted_schedule = sorted(self.schedule)
        for i in sorted_schedule:
            res += f"\n{i} {self.schedule[i]} degrees"

        return res

    def get_target_temperature(self, query_time):

        if len(self.schedule) == 0:
            return self.d_temp

        sorted_schedule = sorted(self.schedule)

        if query_time < sorted_schedule[0]:
            return self.d_temp

        last_time = None
        for i in sorted_schedule:
            if i <= query_time:
                last_time = i
            else:
                break

        if last_time is None:
            return self.d_temp

        return self.schedule[last_time]