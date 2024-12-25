import unittest
from runner_and_tournament import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    def setUp(self):
        self.runner_1 = Runner("Усэйн", 10)
        self.runner_2 = Runner("Андрей", 9)
        self.runner_3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(self):
        for result in self.all_results.values():
            formatted_result = {key: str(value) for key, value in result.items()}
            print(formatted_result)

    def run_tournament_test(self, distance, participants):
        tournament = Tournament(distance, *participants)
        result = tournament.start()
        self.all_results[len(self.all_results) + 1] = result
        slowest_runner = sorted(participants, key=lambda runner: runner.speed)[0]
        self.assertTrue(result[max(result.keys())].name == slowest_runner.name)

    def test_runner_1_runner_2_runner_3(self):
        self.run_tournament_test(90, [self.runner_1, self.runner_2, self.runner_3])

    def test_runner_2_runner_3(self):
        self.run_tournament_test(90, [self.runner_2, self.runner_3])

    def test_runner_1_runner_3(self):
        self.run_tournament_test(90, [self.runner_1, self.runner_3])


if __name__ == "__main__":
    unittest.main()
