# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
  def __init__(self, default_temp=68):
    self.default_temp = default_temp
    self.schedule = {}

  def add_schedule(self, time, temperature):
    self.schedule[time] = temperature

  def __str__(self):
    res = f"Default temperature: {self.default_temp} degrees"
    
    for key, value in sorted(self.schedule.items()):  # Add sorted() here
      res += f"\n{key} {value} degrees"
    
    return res
  

  def get_target_temperature(self, query_time):
    if not self.schedule:
      return self.default_temp

    times = sorted(self.schedule.keys())

    if query_time < times[0]:
      return self.default_temp

    target_temp = self.default_temp
    for time in times:
      if time <= query_time:
        target_temp = self.schedule[time]
      else:
        break

    return target_temp
    



      


