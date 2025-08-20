# sensor.py
"""
Sensor module for the Factory Monitoring System.
Defines the Sensor class representing a physical sensor attached to a machine.
"""

class Sensor:
    """
    @class Sensor
    @brief Represents a sensor (e.g., temperature, pressure, vibration) attached to a machine.
    @details Encapsulates sensor ID, type, and current reading.
    """
    def __init__(self, sensor_id, sensor_type, reading):
        """
        @brief Initialize the Sensor object.
        @param sensor_id The unique identifier for the sensor.
        @param sensor_type The type of the sensor (e.g., Temperature, Pressure, Vibration).
        @param reading The initial reading of the sensor.
        """
        self._id = sensor_id
        self._type = sensor_type
        self._reading = reading

    @property
    def id(self):
        """
        @brief Return the sensor's unique identifier.
        @return The sensor ID.
        """
        return self._id

    @property
    def type(self):
        """
        @brief Return the type of the sensor (e.g., Temperature, Pressure, Vibration).
        @return The sensor type.
        """
        return self._type

    @property
    def reading(self):
        """
        @brief Return the current reading of the sensor.
        @return The current reading value.
        """
        return self._reading

    @reading.setter
    def reading(self, value):
        """
        @brief Set the sensor's reading to a new value.
        @param value The new reading value.
        """
        self._reading = value
