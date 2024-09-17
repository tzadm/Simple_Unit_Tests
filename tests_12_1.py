import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner_1 = Runner('Den')
        for i in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    def test_run(self):
        runner_2 = Runner('Mark')
        for i in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    def test_challenge(self):
        ranner_3 = Runner('Ben')
        ranner_4 = Runner('Sam')
        for i in range(10):
            ranner_3.run()
            ranner_4.walk()
        self.assertNotEqual(ranner_3.distance, ranner_4.distance)


if __name__ == '__main__':
    unittest.main()
