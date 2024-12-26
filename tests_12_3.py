import unittest
from runner import Runner
from runner_and_tournament import Runner, Tournament


def frozen(func):
    def wrapper(atr):
        if atr.is_frozen == True:
            atr.skipTest('Тесты в этом кейсе заморожены')
        else:
            return func
    return wrapper

class RunnerTest(unittest.TestCase):
    is_frozen = False
    @frozen
    def test_walk(self):
        runner = Runner('TestRunner')
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)
    @frozen
    def test_run(self):
        runner = Runner('TestRunner')
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)
    @frozen
    def test_challenge(self):
        runner1 = Runner('Runner1')
        runner2 = Runner('Runner2')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @frozen
    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            formatted_result = {key: str(value) for key, value in result.items()}
            print(formatted_result)
    @frozen
    def run_tournament_test(self, distance, participants):
        tournament = Tournament(distance, *participants)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        slowest_runner = sorted(participants, key=lambda runner: runner.speed)[0]
        self.assertTrue(result[max(result.keys())].name == slowest_runner.name)
    @frozen
    def test_first_tournament(self):
        self.run_tournament_test(90, [self.runner_1, self.runner_2, self.runner_3])

    @frozen
    def test_second_tournament(self):
        self.run_tournament_test(90, [self.runner_2, self.runner_3])

    @frozen
    def test_third_tournament(self):
        self.run_tournament_test(90, [self.runner_1, self.runner_3])

if __name__ == "__main__":
    unittest.main()