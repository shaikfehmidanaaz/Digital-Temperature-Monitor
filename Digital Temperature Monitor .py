# Digital Temperature Monitor
# EEE Mini Project - Python

class DigitalTemperatureMonitor:

    def __init__(self, temperature):
        self.temperature = temperature

    def check_temperature(self):
        if self.temperature < 0:
            return "VERY COLD"
        elif self.temperature < 25:
            return "COLD"
        elif self.temperature < 35:
            return "NORMAL"
        elif self.temperature < 45:
            return "HIGH"
        else:
            return "CRITICAL"

    def display(self):
        status = self.check_temperature()

        print("\n================================")
        print("    DIGITAL TEMPERATURE MONITOR")
        print("================================")
        print(f"Temperature : {self.temperature:.1f} °C")
        print(f"Status      : {status}")

        if self.temperature >= 45:
            print("Warning     : HIGH TEMPERATURE!")
        elif self.temperature >= 35:
            print("Warning     : Temperature is High")
        elif self.temperature < 0:
            print("Warning     : Very Low Temperature")
        else:
            print("Warning     : No Warning")

        print("================================")


# Main program
print("DIGITAL TEMPERATURE MONITOR")

temperature = float(input("Enter temperature (°C): "))

monitor = DigitalTemperatureMonitor(temperature)
monitor.display()
