import unittest
import tests_12_3

mega_Test = unittest.TestSuite()

mega_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))

mega_Test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(mega_Test)
