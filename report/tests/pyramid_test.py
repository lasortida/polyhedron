class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.pyramid = Polyedr("./data/pyramid.geom")

    def test_modification_02(self):
        self.assertEqual(self.pyramid.answer, 4.)
