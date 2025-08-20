# main.py
"""
Main entry point for the Factory Monitoring System.
Loads machine and sensor data from CSV, runs health checks, and demonstrates concurrency.
"""

import csv
from machine import Machine
from sensor import Sensor
from factory_monitor import FactoryMonitor

def load_machines_from_csv(file_path):
    """
    Load machines and their sensors from a CSV file.
    Returns a FactoryMonitor instance populated with machines.
    """
    factory = FactoryMonitor()
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            m = Machine(row["MachineID"])
            if row["Temperature"]:
                m.add_sensor(Sensor("T", "Temperature", float(row["Temperature"])))
            if row["Pressure"]:
                m.add_sensor(Sensor("P", "Pressure", float(row["Pressure"])))
            if row["Vibration"]:
                m.add_sensor(Sensor("V", "Vibration", float(row["Vibration"])))
            factory.add_machine(m)
    return factory

if __name__ == "__main__":
    """
    Run the main program: load data, print health reports, and demonstrate concurrency.
    """
    factory = load_machines_from_csv("machines.csv")

    print("\n🔍 Machine Health Report")
    for machine in factory.machines:
        print(machine.get_status())

    print(f"\n🏭 Average Factory Health: {round(factory.average_health(), 2)}")

    print("\n⚠️ Alerts:")
    for machine in factory.machines:
        if "Critical" in machine.get_status() or "Warning" in machine.get_status():
            print(f" - {machine.get_status()}")

    # Run simulations
    factory.run_sequential(iterations=3)
    factory.run_threaded(iterations=3)
