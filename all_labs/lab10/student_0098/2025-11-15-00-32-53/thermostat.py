# Author   : REDACTED
# Email    : REDACTED
# Spire ID : REDACTED

class Thermostat:
    """
    A programmable thermostat that allows you to adjust room temperatures
    according to a predefined set of schedules.
    """
    def __init__(self, default_temp=68):
        """
        Initializes a Thermostat object.

        Args:
            default_temp (float, optional): The default temperature in Fahrenheit.
                Defaults to 68 degrees.
        """
        self.default_temp = default_temp
        self.schedules = {}
        
class Thermostat:
    def __init__(self, initial_temp):
        self.current_temp = initial_temp
        self.schedules = {}

    def add_schedule(self, time, temperature):
        """
        Adds a new schedule entry or updates an existing one.

        Args:
            time (str): The time in the format 'HH:MM'.
            temperature (float): The temperature value to be associated with the time.

        Returns:
            None
        """
        self.schedules[time] = temperature

class Thermostat:
    def __init__(self, default_temp=68):
        self.default_temp = default_temp
        self.schedules = {}

    def add_schedule(self, time, temp):
        self.schedules[time] = temp

    def __str__(self):
        
        output = f"Default temperature: {self.default_temp} degrees\n"

        
        sorted_schedules = sorted(self.schedules.items(), key=lambda x: x[0])

        
        for time, temp in sorted_schedules:
            output += f"{time} {temp} degrees\n"
        return output.rstrip()
def get_target_temperature(self, query_time):
    """
    Returns the target temperature at the given query time.

    The function assumes that the schedules are sorted in ascending order of time.
    If the query time is earlier than the earliest schedule time, the default temperature is returned.
    If the query time is after the last schedule time, the temperature set at the last time is returned.
    Otherwise, the function returns the temperature corresponding to the latest schedule time that is earlier than or equal to the query time.

    Args:
        query_time (str): The query time in the format 'HH:MM'.

    Returns:
        float: The target temperature at the given query time.
    """
    
    query_minutes = self._time_to_minutes(query_time)

    
    for i in range(len(self.schedules) - 1, -1, -1):
        schedule_time = self._time_to_minutes(self.schedules[i][0])
        if query_minutes >= schedule_time:
            return self.schedules[i][1]

    
    return self.default_temperature

def _time_to_minutes(self, time_str):
    """
    Converts a time string in the format 'HH:MM' to the number of minutes since midnight.

    Args:
        time_str (str): The time string in the format 'HH:MM'.

    Returns:
        int: The number of minutes since midnight.
    """
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes
