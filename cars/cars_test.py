import unittest
import cars

class TestParser(unittest.TestCase):

    def setUp(self):
        self.data = cars.read_file("a_example.in")

    def test_first_line(self):
        self.assertEqual(3, self.data.R)
        self.assertEqual(4, self.data.C)
        self.assertEqual(2, self.data.F)
        self.assertEqual(3, self.data.N)
        self.assertEqual(2, self.data.B)
        self.assertEqual(10, self.data.T)

    def test_rides(self):
        self.assertEqual(3, len(self.data.rides))
        self.assertEqual(0, self.data.rides[0].a)
        self.assertEqual(0, self.data.rides[0].b)
        self.assertEqual(1, self.data.rides[1].x)
        self.assertEqual(0, self.data.rides[1].y)
        self.assertEqual(0, self.data.rides[2].s)
        self.assertEqual(9, self.data.rides[2].f)

class TestSolver(unittest.TestCase):

    def test_solve(self):
        data = cars.read_file("a_example.in")
        print "EXAMPLE"
        cars.solve(data, "a_example.out")


    def test_solve_zoo(self):
        data = cars.read_file("b_should_be_easy.in")
        print "SHOULD BE EASY"
        cars.solve(data, "b_should_be_easy.out")

    def test_solve_trending(self):
        data = cars.read_file("c_no_hurry.in")
        print "NO HURRY"
        cars.solve(data, "c_no_hurry.out")

    def test_solve_spreading(self):
        data = cars.read_file("d_metropolis.in")
        print "PARSING DONE"
        cars.solve(data, "d_metropolis.out")

    def test_solve_kittens(self):
        data = cars.read_file("e_high_bonus.in")
        print "HIGH BONUS"
        cars.solve(data, "e_high_bonus.out")

if __name__ == "__main__":
    TestSolver().test_solve_trending()