# ++++++++++++ LOCAL IMPORTS ++++++++++++#
import operato.keywords.starter as st
import operato.keywords.engine as en
from operato.starter import Starter
from operato.engine import Engine

# Init starter, add necessary comment
starter = Starter()
starter.add(st.XtraLineUser(comment="#RADIOSS STARTER"))
starter.add(st.XtraLineUser(comment="#Test file to demonstrate how to use OPERATO"))
# To set runname:
starter.add(st.Begin(runname="run0"))
# set analysis type:
starter.add(st.Analy(n_2D3D=0, i_parith=0))
# Add Keywords, e.g. MatLaw25
starter.add(
    st.MatLaw25(
        mat_id=1,
        mat_title="blub",
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
starter.add(
    st.PropType10(
        prop_title="bla",
        prop_id=1,
        i_shell=12,
        i_smstr=0,
        i_sh3n=0,
        i_drill=0,
        P_thick_fail=0.0,
        h_m=0.0,
        h_f=0.0,
        h_r=0.0,
        d_m=0.1,
        d_n=0.1,
        N=6,
        Thick=1.8,
        A_shear=0.7,
        i_thick=1,
        i_plas=1,
        V_x=1.0,
        V_y=0.0,
        V_z=1.0,
        skew_id=0,
        i_pos=0,
        i_p=0,
        phi=[-60.0, -30.0, 0.0, 30.0, 60.0],
    )
)
starter.add(
    st.Node(
        node_ids=[0, 1, 2, 3], xc_yc_zc=[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
    )
)
starter.write(assume_yes=True)
########################################################################################
# create engine
engine = Engine()
engine.add(
    en.Run(
        runname="run0",
        run_num=1,
        t_stop=2,
    )
)
engine.add(en.AnimDt(t_start=0, t_freq=2))
engine.write()
