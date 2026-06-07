# Author : REDACTED
# Email : REDACTED
# Spire ID : REDACTED

class Thermostat:
    temp = 68
    def __init__(self, temp):
        self.temp_dict = {}
        try: 
            a = temp
        except TypeError:
            a = 68
        self.temp_dict[a] = " "

    #def add_schedule(self, time, temp):

        #self.schedule = {}
        #self.schedule[time] = temp
        #return self.schedule


    #implement the cast-to-string function
    #def get_target_temperature():


#dev = Thermostat(75)
#dev2 = Thermostat()
#dev.add_schedule('08:00', 60.4)
#dev.add_schedule('19:35', 75.5)
#dev.add_schedule('09:30', 58.2)
#dev.add_schedule('22:39', 68.2)

#print(dev.temp)
#print(temp_dict)

class Thermo:
    def __init__(self):
        self.temp = 68
    def add_schedule(self, time, temp):
        sched_dict = {}
        sched_dict[time] = temp
        return sched_dict


dev = Thermo()
dev.temp = 75
dev.add_schedule('08:00', 60.4)
print(dev)