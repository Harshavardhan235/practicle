# machine.py
"""
Machine module for the Factory Monitoring System.
Defines the Machine class representing a factory machine with sensors.
"""

from sensor import Sensor

class Machine:
    """
    @class Machine
    @brief Represents a factory machine.
    @details Aggregates Sensor objects, computes health, and provides status alerts.
    """
    def __init__(self, machine_id):
        """
        @brief Initialize the Machine object.
        @param machine_id The unique identifier for the machine.
        """
        self.machine_id = machine_id
        self.sensors = {}

    def add_sensor(self, sensor: Sensor):
        """
        @brief Add a Sensor object to the machine.
        @param sensor The Sensor object to add.
        """
        self.sensors[sensor.type] = sensor

    def compute_health(self):
        """
        @brief Compute the health of the machine using sensor readings.
        @details Returns a value between 0 and 100. Raises ValueError if a sensor is missing.
        @return The health value as a float.
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
        @brief Return a string describing the machine's health status or alert.
        @return Status string for the machine.
        """
        try:
            health = self.compute_health()
            if health < 50:
                return f"Machine {self.machine_id}: Critical Machine Failure Risk"
            else:
                return f"Machine {self.machine_id}: Health OK ({round(health,2)})"
        except ValueError as e:
            return f"Machine {self.machine_id}: {str(e)}"
