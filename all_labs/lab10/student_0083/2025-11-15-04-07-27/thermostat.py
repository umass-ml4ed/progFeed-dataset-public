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
        # Convert query_time 'HH:MM' → minutes since midnight
        qh, qm = map(int, query_time.split(':'))
        query_minutes = qh * 60 + qm

        # Sort schedule times
        times = sorted(self.schedules.keys())     # each time is "HH:MM"

        latest_time_before = None

        for t in times:
            th, tm = map(int, t.split(':'))
            t_minutes = th * 60 + tm

            if t_minutes <= query_minutes:
                latest_time_before = t
            else:
                break

        # Case 1: no schedule earlier than query → return default
        if latest_time_before is None:
            return self.default_temperature

        # Case 2: return temperature of the latest time ≤ query
        return self.schedules[latest_time_before]

            



            
        
dev = Thermostat(75)
dev.add_schedule('08:00', 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)

print(dev)