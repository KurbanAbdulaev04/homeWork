import unittest
from required_file import rt_with_exceptions as rwe


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(self):
        self.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.runer_1 = rwe.Runner('Усэйн', 10)
        self.runer_2 = rwe.Runner('Андрей', 9)
        self.runer_3 = rwe.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        for i in self.all_results:
            print(i)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_runer_1(self):
        tour = rwe.Tournament(90, self.runer_1, self.runer_3)
        tour_1 = tour.start()
        self.all_results.append(tour_1)
        self.assertTrue(tour_1[len(tour_1)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_runer_2(self):
        tour = rwe.Tournament(90, self.runer_2, self.runer_3)
        tour_2 = tour.start()
        self.all_results.append(tour_2)
        self.assertTrue(tour_2[len(tour_2)] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start_runer_3(self):
        tour = rwe.Tournament(90, self.runer_2, self.runer_1, self.runer_3)
        tour_3 = tour.start()
        self.all_results.append(tour_3)
        self.assertTrue(tour_3[len(tour_3)] == 'Ник')
