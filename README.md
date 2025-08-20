# 🏭 Factory Monitoring System

## 📌 Introduction
This project is an **OOP-based Factory Health Monitoring System** designed to track and assess the health of industrial machines using sensor data. It demonstrates best practices in encapsulation, modular design, and scalability, making it easy to extend and maintain.
## ⚙️ Classes
- **Sensor**: Represents a physical sensor (e.g., temperature, pressure, vibration) attached to a machine. Encapsulates sensor ID, type, and current reading.
- **Machine**: Models a factory machine. Aggregates multiple `Sensor` objects, computes machine health using a weighted formula, and provides status alerts for critical conditions or missing sensors.
- **FactoryMonitor**: Manages a collection of machines, calculates average factory health, and supports both sequential and threaded (concurrent) simulation of sensor updates.
## ▶️ Usage
- **Run the project:**
	```sh
	python main.py
	```
- **Run tests:**
	```sh
	pytest -v
	```
## 📂 Example
### Sample CSV Input (`machines.csv`):
```
MachineID,Temperature,Pressure,Vibration
M1,50,100,0.2
M2,80,150,0.4
M3,90,200,0.5
```
### Expected Output (partial):
```
🔍 Machine Health Report
Machine M1: Health OK (44.0)
Machine M2: Critical Machine Failure Risk
Machine M3: Critical Machine Failure Risk

🏭 Average Factory Health: 15.0

⚠️ Alerts:
 - Machine M2: Critical Machine Failure Risk
 - Machine M3: Critical Machine Failure Risk

🔄 Running Sequential Simulation
[Seq] M1 health: ...
...
⚡ Running Threaded Simulation
[Thread] M1 health: ...
...
```
## 🔄 Concurrency
The system supports both **sequential** and **threaded** (concurrent) simulation of sensor data updates, demonstrating scalable monitoring for real-world factory environments.

----
**Keywords:** encapsulation, modular design, scalability, OOP, factory monitoring, concurrency
