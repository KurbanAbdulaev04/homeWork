import unittest
from required_file.rt_with_exceptions import Runner as Run_1


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        class_obj_walk = Run_1('Name')
        for _ in range(10):
            class_obj_walk.walk()
        self.assertEqual(class_obj_walk.distance, 50)

    def test_run(self):
        class_obj_run = Run_1('Name')
        for _ in range(10):
            class_obj_run.run()
        self.assertEqual(class_obj_run.distance, 100)

    def test_challenge(self):
        challenger_1 = Run_1('1')
        challenger_2 = Run_1('2')
        for _ in range(10):
            challenger_1.run()
            challenger_2.walk()
        self.assertNotEqual(challenger_1.distance, challenger_2.distance)
