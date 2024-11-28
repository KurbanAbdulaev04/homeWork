import logging
import unittest
from required_file.rt_with_exceptions import Runner as Run_1

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='UTF-8',
                    format="%(asctime)s <-> %(levelname)s <-> %(message)s")


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            class_obj_walk = Run_1('Name', -3)
            logging.info('"test_walk" выполнен успешно')
            for _ in range(10):
                class_obj_walk.walk()
            self.assertEqual(class_obj_walk.distance, 50)
        except Exception as err:
            logging.warning('Неверная скорость для Runner', exc_info=True)
            return 0

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            class_obj_run = Run_1(True)
            logging.info('"test_run" выполнен успешно')
            for _ in range(10):
                class_obj_run.run()
            self.assertEqual(class_obj_run.distance, 100)
        except Exception as err:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        challenger_1 = Run_1('1')
        challenger_2 = Run_1('2')
        for _ in range(10):
            challenger_1.run()
            challenger_2.walk()
        self.assertNotEqual(challenger_1.distance, challenger_2.distance)
