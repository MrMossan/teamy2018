import unittest
import caching

class TestParser(unittest.TestCase):

    def setUp(self):
        self.data = caching.read_file("example.in")

    def test_first_line(self):
        self.assertEqual(5, self.data.V)
        self.assertEqual(2, self.data.E)
        self.assertEqual(4, self.data.R)
        self.assertEqual(3, self.data.C)
        self.assertEqual(100, self.data.X)

    def test_video_sizes(self):
        self.assertEqual(50, self.data.video_sizes[0])
        self.assertEqual(110, self.data.video_sizes[-1])

    def test_endpoints(self):
        self.assertEqual(1000, self.data.endpoints[0].Ld)
        self.assertEqual(3, len(self.data.endpoints[0].caches))
        self.assertEqual(1, self.data.endpoints[0].caches[2].c)
        self.assertEqual(200, self.data.endpoints[0].caches[1].Lc)

