# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default = 68):
        self.temp = default
        self.schedule = {}
    
    def add_schedule(self, time, temperature):
        self.schedule[time] = temperature

    def __str__(self):
        output_line = f"Default temperature: {self.temp} degrees"
        for key in sorted(self.schedule):
            output_line += f"\n{key} {self.schedule[key]} degrees"
        return output_line

    def get_target_temperature(self, query):
        list_of_keys = sorted(self.schedule)
        list_of_times = [key.split(":") for key in list_of_keys]
        list_of_minutes = [int(item[0])*60+int(item[1]) for item in list_of_times]
        query_minutized_list = query.split(":")
        query_minitized = int(query_minutized_list[0])*60 + int(query_minutized_list[1])
        if query_minitized < list_of_minutes[0] or len(list_of_minutes) == 0:
            return self.temp
        for index in range(len(list_of_minutes)-1):
            if query_minitized - list_of_minutes[index] >= 0 and query_minitized - list_of_minutes[index+1] < 0:
                return self.schedule[list_of_keys[index]]
        return self.schedule[list_of_keys[-1]]

therm = Thermostat()
print(therm)
therm.add_schedule("06:00", 70)
therm.add_schedule("09:00", 65)
therm.add_schedule("17:00", 72)
therm.add_schedule("22:00", 66)
# print(therm.get_target_temperature("08:30"))  # 70
# print(therm.get_target_temperature("23:00"))  # 66
# print(therm.get_target_temperature("03:00"))