# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    def __init__(self, default=68.0, schedule={}):
        if schedule is None:
            schedule = dict()
        self.schedule = schedule
        self.default = default

    def add_schedule(self, time: str, temperature: float):
        newDict = {time: temperature}
        self.schedule.update(newDict)

    def __str__(self):
        try:
            defTemp = int(self.default)
        except ValueError:
            defTemp = self.default
        returnString = f"Default temperature: {defTemp} degrees\n"
        timeList = sorted(self.schedule)
        for times in timeList:
            try:
                times = int(times)
                returnString += f"{times} {self.schedule[times]} degrees\n"
            except:

                returnString += f"{times} {self.schedule[times]} degrees\n"
        return returnString.rstrip()

    def get_target_temperature(self, qTime):
        timeSet = set(self.schedule.keys())

        timeList = sorted(timeSet)
        #print(timeList)
        if qTime in timeList:
            return self.schedule[qTime]
        elif timeList[0] == qTime or timeList[0] >= qTime:
            return self.default

        else:
            timeList.append(qTime)
            timeList.sort()
            for time in range(len(timeList)):
                if timeList[time] == qTime:
                    return self.schedule[timeList[time -1]]

        # if qTime < timeList[0]:
        #     return self.default
        # elif qTime > timeList[-1]:
        #     return timeList[-1]
        # else:
        #     for times in range(len(timeList[0:-1])):
        #         if qTime == timeList[times]:
        #             return timeList[times]
        #         elif qTime >= timeList[times] and qTime < timeList[times + 1]:
        #             return timeList[times]

print(Thermostat())
dev = Thermostat(75.0)
dev.add_schedule("08:00", 60.4)
dev.add_schedule('19:35', 75.5)
dev.add_schedule('09:30', 58.2)
dev.add_schedule('22:39', 68.2)
print(dev.get_target_temperature('23:00') )
print(dev.get_target_temperature('16:35'))
print(dev.get_target_temperature('05:55'))
print(dev.get_target_temperature('08:00'))
print(dev.get_target_temperature('12:00'))
print(dev)

