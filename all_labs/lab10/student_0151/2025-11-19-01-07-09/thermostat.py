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
    list_schedule = [f"{key} {value} degrees\n" for key,value in self.schedule.items()]
    res = f"""
      Default temperature: {self.default_temp} degrees
      {",".split(list_schedule)}
      """
    return res
  

  def get_target_temperature(self, query_time):
    if not self.schedule:
      return self.default_temp

    times = sorted(self.schedule.keys())

    if query_time < times[0]:
        return self.default_temp

    for i in range(len(times)):
      if query_time > times[i]:
        return self.schedule[times[i-1]]
    
    return self.schedule[times[-1]]

        

    



      


