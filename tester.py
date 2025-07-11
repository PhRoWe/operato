# ++++++++++++ LOCAL IMPORTS ++++++++++++#
import operato.keywords.starter as st
import operato.keywords.engine as en
from operato.starter import Starter
from operato.engine import Engine

starter = Starter()
starter.add(st.XtraLineUser(comment="#-  2. MATERIALS:"))
# for beams: use Law2 instead of Law1
mat_id = 1
starter.add(
    st.MatLaw12(
        mat_id=mat_id,
        mat_title="",
        rho=7.8e-6,
        E11=2.1e2,
        E22=2.1e2,
        E33=2.1e2,
        nu12=0.2,
        nu13=0.3,
        nu23=0.1,
        G12=0.7e-2,
        G13=0.7e-2,
        G23=0.7e-2,
        B=1,
        alpha=0,
        Ef=100,
        depsdt_0=0.01,
    )
)

starter.add(
    st.MatLaw14(
        mat_id=mat_id,
        mat_title="",
        rho=7.8e-6,
        E11=2.1e2,
        E22=2.1e2,
        E33=2.1e2,
        nu12=0.2,
        nu13=0.3,
        nu23=0.1,
        G12=0.7e-2,
        G13=0.7e-2,
        G23=0.7e-2,
        B=1,
        alpha=0,
        Ef=100,
        depsdt_0=0.01,
    )
)
starter.add(
    st.FunctSmooth(
        fct_id=1,
        fct_title="blaabla",
        x=[0, 0.4, 1.0],
        y=[0, 1.0, 1.0],
    )
)
starter.add(
    st.FunctSmooth(
        fct_id=1,
        fct_title="blaabla",
        Ascalex=2.0,
        Fscaley=1.9,
        x=[0, 0.4, 1.0],
        y=[0, 1.0, 1.0],
    )
)
starter.add(
    st.Node(
        node_ids=[0, 1],
        xc_yc_zc=[[0, 0, 0], [1, 1, 1]],
    )
)

starter.write(assume_yes=True)
