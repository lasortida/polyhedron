class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.cube = Polyedr("./data/cube.geom")

    def test_modification_03(self):
        self.assertEqual(self.cube.answer, 12.)
