# sensor.py
"""
Sensor module for the Factory Monitoring System.
Defines the Sensor class representing a physical sensor attached to a machine.
"""

class Sensor:
    """
    Represents a sensor (e.g., temperature, pressure, vibration) attached to a machine.
    Encapsulates sensor ID, type, and current reading.
    """
    def __init__(self, sensor_id, sensor_type, reading):
        self._id = sensor_id
        self._type = sensor_type
        self._reading = reading

    @property
    def id(self):
        """Return the sensor's unique identifier."""
        return self._id

    @property
    def type(self):
        """Return the type of the sensor (e.g., Temperature, Pressure, Vibration)."""
        return self._type

    @property
    def reading(self):
        """Return the current reading of the sensor."""
        return self._reading

    @reading.setter
    def reading(self, value):
        """Set the sensor's reading to a new value."""
        self._reading = value
