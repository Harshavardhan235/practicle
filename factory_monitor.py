# factory_monitor.py
"""
FactoryMonitor module for the Factory Monitoring System.
Defines the FactoryMonitor class for managing machines and concurrency.
"""

import threading
import time
import random
from machine import Machine

class FactoryMonitor:
    """
    Manages a collection of Machine objects in the factory.
    Provides methods for average health calculation and simulating sensor updates
    both sequentially and with threading for concurrency.
    """
    def __init__(self):
        self.machines = []
        self.lock = threading.Lock()

    def add_machine(self, machine: Machine):
        """Add a Machine object to the factory."""
        self.machines.append(machine)

    def average_health(self):
        """Return the average health of all machines in the factory."""
        if not self.machines:
            return 0.0
        total = 0
        for m in self.machines:
            total += m.compute_health()
        return total / len(self.machines)

    def run_sequential(self, iterations=3):
        """
        Simulate sequential sensor updates for all machines.
        Each machine's sensors are updated in sequence.
        """
        print("\n🔄 Running Sequential Simulation")
        for i in range(iterations):
            for machine in self.machines:
                for s in machine.sensors.values():
                    s.reading += random.uniform(-5, 5)  # small fluctuation
                health = machine.compute_health()
                print(f"[Seq] {machine.machine_id} health: {round(health, 2)}")
            time.sleep(1)

    def run_threaded(self, iterations=3):
        """
        Simulate concurrent sensor updates using threads.
        Each machine's sensors are updated in parallel threads.
        """
        print("\n⚡ Running Threaded Simulation")

        def update_machine(machine: Machine):
            for i in range(iterations):
                with self.lock:  # ensure thread-safe updates
                    for s in machine.sensors.values():
                        s.reading += random.uniform(-5, 5)
                    health = machine.compute_health()
                print(f"[Thread] {machine.machine_id} health: {round(health, 2)}")
                time.sleep(1)

        threads = []
        for m in self.machines:
            t = threading.Thread(target=update_machine, args=(m,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
