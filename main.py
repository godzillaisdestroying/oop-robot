# Define the Robot class
class Robot:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year
    
    def introduce(self):
        print(f"Hello! I am {self.name}, a {self.model} model robot.")
        print(f"I was created in the year {self.year}.")
    
    def perform_task(self, task):
        print(f"{self.name} is now performing: {task}")

# Create a specialized class for Jack the Robot
class JackRobot(Robot):
    def __init__(self):
        # Initialize with specific values for Jack
        super().__init__(name="Jack", model="XTR-2024", year=2024)

    def introduce_jack(self):
        print("Initiating self-introduction protocol...")
        self.introduce()

# Example usage
if __name__ == "__main__":
    jack = JackRobot()  # Create an instance of Jack the Robot
    jack.introduce_jack()  # Introduce Jack
    jack.perform_task("sweeping the floor")  # Make Jack perform a task
