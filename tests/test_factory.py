# tests/test_factory.py
import pytest
from sensor import Sensor
from machine import Machine
from factory_monitor import FactoryMonitor

# Test 1: Machine with health < 50 should raise critical alert
def test_critical_alert():
    m = Machine("M1")
    m.add_sensor(Sensor("T1", "Temperature", 120))
    m.add_sensor(Sensor("P1", "Pressure", 250))
    m.add_sensor(Sensor("V1", "Vibration", 1.5))
    assert "Critical" in m.get_status()

# Test 2: Machine with missing sensor should raise ValueError
def test_missing_sensor():
    m = Machine("M2")
    m.add_sensor(Sensor("T1", "Temperature", 100))
    # Missing Pressure + Vibration
    with pytest.raises(ValueError, match="Sensor Offline Warning"):
        m.compute_health()

# Test 3: Factory average health with multiple machines
def test_average_health():
    f = FactoryMonitor()

    m1 = Machine("M1")
    m1.add_sensor(Sensor("T1", "Temperature", 80))
    m1.add_sensor(Sensor("P1", "Pressure", 200))
    m1.add_sensor(Sensor("V1", "Vibration", 0.5))

    m2 = Machine("M2")
    m2.add_sensor(Sensor("T2", "Temperature", 130))
    m2.add_sensor(Sensor("P2", "Pressure", 300))
    m2.add_sensor(Sensor("V2", "Vibration", 2.0))

    f.add_machine(m1)
    f.add_machine(m2)

    # Correct expected value
    assert round(f.average_health(), 2) == 15.00

# Test 4: Boundary condition health = 50 should NOT be critical
def test_boundary_health_50():
    m = Machine("M3")
    m.add_sensor(Sensor("T1", "Temperature", 100))  # 100/2 = 50
    m.add_sensor(Sensor("P1", "Pressure", 0))       # 0/10 = 0
    m.add_sensor(Sensor("V1", "Vibration", 0))      # 0*20 = 0
    assert "Critical" not in m.get_status()

# Test 5: Empty factory should return average = 0.0
def test_empty_factory():
    f = FactoryMonitor()
    assert f.average_health() == 0.0
