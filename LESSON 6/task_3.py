class StepCounter:

    def __init__(self, steps = 0):
        self.steps = steps

    def step(self):
        self.steps += 1

    def walk(self, distance_steps):
        self.distance_steps = distance_steps
        self.steps += distance_steps

    def reset(self):
        self.steps = 0

    def get_distance_km(self):
        end_steps = self.steps * 0.75 / 1000
        return end_steps

Step = StepCounter()
Step.walk(int(input("Введіть зазначену к-сть кроків: ")))

print(f"Пройдена відстань у км: {Step.get_distance_km()}")
print()

Step.reset()
print(f"Після скиду: {Step.steps} кроків")