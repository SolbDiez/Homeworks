from homework_12_1 import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        pasha = Runner('Pasha')
        for i in range(10):
            pasha.walk()
        self.assertEqual(pasha.distance, 50)
    def test_run(self):
        lena = Runner('Lena')
        for i in range(10):
            lena.run()
        self.assertEqual(lena.distance, 100)
    def test_challenge(self):
        lena = Runner('Lena')
        pasha = Runner('Pasha')
        for i in range(10):
            lena.run()
            pasha.walk()
        self.assertNotEqual(lena.distance, pasha.distance)


if __name__ == '__main__':
    unittest.main()


