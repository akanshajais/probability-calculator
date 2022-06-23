import copy
import random
# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, number in kwargs.items():
            for i in range(number):
                self.contents.append(color)

    def draw(self, number):
        """Receive number of balls to get from contents, remove it from contents randomly and return them"""

        if number > len(self.contents):
            return self.contents

        result = []
        for i in range(number):
            random_ball = random.randrange(0, len(self.contents))
            result.append(self.contents[random_ball])
            self.contents.pop(random_ball)

        return result


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for i in range(num_experiments):
        exp_hat = copy.deepcopy(hat)

        drawn_balls = exp_hat.draw(num_balls_drawn)

        good_exp = True
        for color, number in expected_balls.items():
            ball_num_in_draw = drawn_balls.count(color)
            if ball_num_in_draw < number:
                good_exp = False
                break

        if good_exp:
            success += 1

    return success / num_experiments
