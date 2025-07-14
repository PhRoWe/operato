import unittest
import os
from operato.starter import Starter
from operato.engine import Engine
from operato.keywords.engine import *
from operato.keywords.starter import *
import tempfile


class TestModule(unittest.TestCase):

    # def tearDown(self):
    #     # This method is called after each test
    #     # Clean up: Delete the file
    #     if os.path.exists(self.test_file.name):
    #         os.remove(self.test_file.name)

    # def test_starter_basic(self):
    #     self.test_file = tempfile.NamedTemporaryFile(delete=False)
    #     self.test_file.name = "_0000.rad"
    #     starter = Starter()
    #     starter.write()

    def test_engine_basic(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.name = "_0001.rad"
        engine = Engine()
        # engine.add(AnimDt(t_start=0.0, t_freq=1.0, t_stop=2.0))
        engine.add(DtAms(Iflag=0, dTmin=0.01))
        engine.add(DtAms(dTmin=0.01, Iflag=1, Tol_AMS=3))
        engine.add(DtAms(dTmin=0.01, Iflag=2, Niter=4, Nprint=1))
        engine.write()

    def test_MPC(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.name = "MPC.rad"
        starter = Starter()
        starter.add(
            Mpc(
                id=0,
                title="hhjff",
                node_id=[1, 2],
                idof=[1, 3],
                skew_id=[1, 2],
                alpha=[3, 3],
            )
        )
        starter.write()

    def test_DtNodaKeyword3Iflag(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.name = "DtNoda.rad"
        engine = Engine()
        engine.add(DtNodaKeyword3Iflag(Keyword3="CST", dTmin=0.9, dT_sca=0.1))
        engine.add(
            DtNodaKeyword3Iflag(
                Keyword3="CST",
                dTmin=0.9,
                dT_sca=0.1,
                Iflag=0,
                initial_mass_ratio=0,
                grnd_ID=4,
            )
        )
        engine.write()

    def test_FunctSmooth(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.name = "DtNoda.rad"
        starter = Starter()
        starter.add(
            FunctSmooth(
                fct_id=1,
                fct_title="blaabla",
                x=[0, 0.4, 1.0],
                y=[0, 1.0, 1.0],
            )
        )
        starter.add(
            FunctSmooth(
                fct_id=1,
                fct_title="blaabla",
                Ascalex=2.0,
                Fscaley=1.9,
                x=[0, 0.4, 1.0],
                y=[0, 1.0, 1.0],
            )
        )
        starter.write()

    def test_MatLaw25(self):
        self.test_file = tempfile.NamedTemporaryFile(delete=False)
        self.test_file.name = "matLaw25.rad"
        starter = Starter()
        starter.add(
            MatLaw25(
                mat_id=1,
                mat_title="test123",
                rho=7.8e-6,
                E11=2.1e2,
                E22=2.1e2,
                E33=2.1e2,
                nu12=0.3,
                G12=0.7e-2,
                G13=0.7e-2,
                G23=0.7e-2,
                i_off=0,
                depsdt0=0.01,
            )
        )
        starter.write()


if __name__ == "__main__":
    unittest.main()
