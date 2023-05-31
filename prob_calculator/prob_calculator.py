import random
from collections import Counter

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball] * count)

    def draw(self, num_balls):
        num_balls = min(num_balls, len(self.contents))
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0

    for _ in range(num_experiments):
        hat_copy = Hat(**dict(Counter(hat.contents)))  # Create a new Hat object with the same contents
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = Counter(drawn_balls)

        success = True
        for ball, count in expected_balls.items():
            if drawn_balls_count[ball] < count:
                success = False
                break

        if success:
            num_success += 1

    probability = num_success / num_experiments
    return probability

# Example usage
hat = Hat(blue=5, red=4, green=2)
expected_balls = {"red": 1, "green": 2}
num_balls_drawn = 4
num_experiments = 10000

probability = experiment(hat, expected_balls, num_balls_drawn, num_experiments)
print(f"Probability: {probability}")
