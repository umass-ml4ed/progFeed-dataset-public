# Author : REDACTED
# Email: REDACTED
# Spire ID: REDACTED

# Thermostat class to allow a user to add schedules and later query the schedules 
# to find the target temperature given an arbitrary time.
class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    """
    store the time-temperature pair (where time is the key and temperature is the value) 
    in the schedules dictionary. If the time already exists, its value will be overwritten 
    by the new temperature; otherwise it will create a new entry. 
    """
    def add_schedule(self, time_str, temperature):
        self.schedules[time_str] = temperature

    #Casts this object to a string. Returns a string
    def __str__(self):
        result = "Default temperature: " + str(self.default_temp) + " degrees"
        times = sorted(self.schedules)
        for t in times:
            result += "\n" + t + " " + str(self.schedules[t]) + " degrees"
        return result

    """
    should take an arbitrary query time (string) as the parameter, and it should return 
    the target temperature at that query time. 
    """
    def get_target_temperature(self, query_time):
        if self.schedules == {}:
            return self.default_temp
        times = sorted(self.schedules)
        latest = None
        for t in times:
            if t <= query_time:
                latest = t
            else:
                break
        if latest is None:
            return self.default_temp
        else:
            return self.schedules[latest]
#dev = Thermostat(75)
#dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)
#print(Thermostat())
#print(dev)
#dev.get_target_temperature('23:00') #returns 68.2
#dev.get_target_temperature('16:35') #returns 58.2
#dev.get_target_temperature('05:55') #returns 75
#dev.get_target_temperature('08:00') #returns 60.4
#dev.get_target_temperature('12:00') #returns 58.2


