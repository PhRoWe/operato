import unittest
import os
from operato.starter import Starter
from operato.engine import Engine
from operato.keywords.engine import *
from operato.keywords.starter import *
import tempfile


class TestModule(unittest.TestCase):

    def tearDown(self):
        # This method is called after each test
        # Clean up: Delete the file
        if os.path.exists(self.test_file.name):
            os.remove(self.test_file.name)

    def test_starter_basic(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.name = "_0000.rad"
        starter = Starter()
        starter.write()

    def test_engine_basic(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.name = "_0001.rad"
        engine = Engine()
        engine.add(AnimDt(t_start=0.0, t_freq=1.0, t_stop=2.0))
        engine.add(DtAms(Iflag=0, dTmin=0.01))
        engine.add(DtAms(dTmin=0.01, Iflag=1, Tol_AMS=3))
        engine.add(DtAms(dTmin=0.01, Iflag=2, Niter=4, Nprint=1))
        engine.write()


if __name__ == "__main__":
    unittest.main()
