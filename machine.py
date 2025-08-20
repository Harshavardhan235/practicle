# machine.py
"""
Machine module for the Factory Monitoring System.
Defines the Machine class representing a factory machine with sensors.
"""

from sensor import Sensor

class Machine:
    """
    Represents a factory machine.
    Aggregates Sensor objects, computes health, and provides status alerts.
    """
    def __init__(self, machine_id):
        self.machine_id = machine_id
        self.sensors = {}

    def add_sensor(self, sensor: Sensor):
        """Add a Sensor object to the machine."""
        self.sensors[sensor.type] = sensor

    def compute_health(self):
        """
        Compute the health of the machine using sensor readings.
        Returns a value between 0 and 100. Raises ValueError if a sensor is missing.
        """
        try:
            temp = self.sensors["Temperature"].reading
            pressure = self.sensors["Pressure"].reading
            vibration = self.sensors["Vibration"].reading
        except KeyError:
            raise ValueError("Sensor Offline Warning")

        health = 100 - (temp/2 + pressure/10 + vibration*20)
        return max(0, health)  # clamp negative health to 0

    def get_status(self):
        """
        Return a string describing the machine's health status or alert.
        """
        try:
            health = self.compute_health()
            if health < 50:
                return f"Machine {self.machine_id}: Critical Machine Failure Risk"
            else:
                return f"Machine {self.machine_id}: Health OK ({round(health,2)})"
        except ValueError as e:
            return f"Machine {self.machine_id}: {str(e)}"
