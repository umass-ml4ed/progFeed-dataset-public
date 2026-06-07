# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self,default_temp=68):
        self.default_temp = default_temp
        self.scheduled_temps = {}
    def add_schedule(self,time=str,temp=float):
        self.scheduled_temps[time] = temp
    
    def list_schedules(self):
        self.listed = sorted(self.scheduled_temps)
    def __str__(self):
    
        result = f"Default temperature: {self.default_temp} degrees"
        if not self.scheduled_temps:
            return result
        for time in sorted(self.scheduled_temps):
            temp = self.scheduled_temps[time]
            result += f"\n{time} {temp} degrees"

        return result   

    def get_target_temperature(self, query_time):
        # Convert query_time 'HH:MM' → total minutes since midnight
        qh, qm = map(int, query_time.split(':'))
        query_minutes = qh * 60 + qm

        # Sort schedule times (strings)
        times = sorted(self.scheduled_temps.keys())

        latest_time_before = None

        for t in times:
            th, tm = map(int, t.split(':'))
            t_minutes = th * 60 + tm

            if t_minutes <= query_minutes:  
                latest_time_before = t
            else:
                break

        # No schedule earlier than query → return default temperature
        if latest_time_before is None:
            return self.default_temp

        # Otherwise return temperature at that schedule
        return self.scheduled_temps[latest_time_before]
