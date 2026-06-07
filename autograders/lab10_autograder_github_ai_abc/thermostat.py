# thermostat.py

class Thermostat:
    def __init__(self, default_temp=68):
        """
        Constructor for the Thermostat class.
        Initializes the default temperature and an empty schedule dictionary.
        """
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        """
        Adds or updates a time-temperature pair in the schedule.
        """
        self.schedules[time] = temperature

    def __str__(self):
        """
        Returns a string representation of the thermostat’s settings.
        """
        result = f"Default temperature: {self.default_temp} degrees"
        if not self.schedules:
            return result

        # Sort times in ascending order
        for time in sorted(self.schedules):
            temp = self.schedules[time]
            result += f"\n{time} {temp} degrees"
        return result

    def get_target_temperature(self, query_time):
        """
        Returns the temperature at the given query time based on the schedule.
        """
        if not self.schedules:
            return self.default_temp

        # Get sorted times
        sorted_times = sorted(self.schedules.keys())

        # If query time is earlier than the first schedule → default temperature
        if query_time < sorted_times[0]:
            return self.default_temp

        # Iterate through sorted times to find the most recent applicable schedule
        target_time = sorted_times[0]
        for t in sorted_times:
            if t <= query_time:
                target_time = t
            else:
                break

        return self.schedules[target_time]

if __name__ == '__main__':
    # Create a thermostat with a custom default temperature
    dev = Thermostat(75)

    # Add schedules (unordered)
    dev.add_schedule('08:00', 60.4)
    dev.add_schedule('19:35', 75.5)
    dev.add_schedule('09:30', 58.2)
    dev.add_schedule('22:39', 68.2)

    # Print the object
    print(dev)

    # Test queries
    print(dev.get_target_temperature('23:00'))  # Expected 68.2
    print(dev.get_target_temperature('16:35'))  # Expected 58.2
    print(dev.get_target_temperature('05:55'))  # Expected 75
    print(dev.get_target_temperature('08:00'))  # Expected 60.4
    print(dev.get_target_temperature('12:00'))  # Expected 58.2
