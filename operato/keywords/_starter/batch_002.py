#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal, List, Sequence
from numpy.typing import NDArray

from operato.keywords.common import (
    ArrayOfAtomicFields,
    BoolField,
    FloatField,
    IntField,
    Keyword,
    StringField,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ALE/MUSCL                  /ALE/SOLVER/FINT            /AMS
# /ANALY                      /ANIM/VERS                  /BCS
# /BCS/CYCLIC                 /BCS/LAGMUL                 /BEAM
#


# --- /ALE/MUSCL ------------------------------------------------------------------------------
@dataclass
class ALEMuscl(Keyword):
    """Allows for a second order monotonic upstream-centered scheme for
    conservation laws (MUSCL) reconstruction of volume fraction fields when
    using multi-material laws and for full full second order scheme (time and
    space) when using material law LAW151.
    (https://2022.help.altair.com/2022/hwsolvers/rad/topics/solvers/rad/ale_muscl_starter_r.htm)
    """

    beta: float
    iflag: Literal[0, 1] = 0
    add_header: bool = True

    @property
    def keyword(self):
        return "/ALE/MUSCL"

    @property
    def pre_conditions(self):
        return [
            (0.0 < self.beta < 2.0, "Pre-condition `0.0 < beta < 2.0` is violated.")
        ]

    @property
    def structure(self):
        structure = [[FloatField("beta", 1), IntField("iflag", 3)]]

        return structure


# --- /ALE/SOLVER/FINT ------------------------------------------------------------------------
@dataclass
class ALESolverFint(Keyword):
    """This option defines the numerical method for internal force
    integration.  This is relevant only for brick element and ALE legacy solver
    (momentum equation solved with FEM).
    (https://2022.help.altair.com/2022/hwsolvers/rad/topics/solvers/rad/ale_solver_fint_starter_r.htm)
    """

    iform: Literal[0, 1, 2, 3] = 3
    add_header: bool = True

    @property
    def keyword(self):
        return "/ALE/SOLVER/FINT"

    @property
    def pre_conditions(self):
        return [
            (
                self.iform in {0, 1, 2, 3},
                "Pre-condition `iform in {0,1,2,3} is violated.",
            )
        ]

    @property
    def structure(self):
        structure = [IntField("iform", 1)]

        return structure


# --- /AMS ------------------------------------------------------------------------------------
@dataclass
class Ams(Keyword):
    """Describes the part group on which the advanced mass scaling is applied.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/ams_starter_r.htm)
    """

    grpart_id: int
    add_header: bool = True

    @property
    def keyword(self):
        return "/AMS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [IntField("grpart_id", 1)]

        return structure


# --- /ANALY ----------------------------------------------------------------------------------
@dataclass
class Analy(Keyword):
    """Defines the type of analysis and sets analysis flags.
    (https://2022.help.altair.com/2022/hwsolvers/rad/topics/solvers/rad/analy_starter_r.htm)
    """

    n_2D3D: Literal[0, 1, 2] = 0
    """Analysis type: 0: 3D, 1: Axisymmetric, 2: Plane Strain"""
    i_parith: Literal[0, 1, 2] = 0
    i_subcycle: Literal[0, 2] = 0
    # FIXME: i_subcycle removed in V2024!
    add_header: bool = True

    @property
    def keyword(self):
        return "/ANALY"

    @property
    def pre_conditions(self):
        return [
            (
                self.n_2D3D in {0, 1, 2},
                "Pre-condtion `n_2D3D in {0, 1, 2} is violated.",
            ),
            (
                self.i_parith in {0, 1, 2},
                "Pre-condtion `i_parith in {0, 1, 2} is violated.",
            ),
            (
                self.i_subcycle in {0, 2},
                "Pre-condtion `i_subcycle in {0, 2} is violated.",
            ),
        ]

    @property
    def structure(self):
        return [
            IntField("n_2D3D", 1),
            IntField("i_parith", 3),
            IntField("i_subcycle", 4),
        ]


# --- /ANIM/VERS ------------------------------------------------------------------------------
@dataclass
class AnimVers(Keyword):
    """Defines the animation file version."""

    anim_vers: int = 44
    add_header: bool = True

    @property
    def keyword(self):
        return "/ANIM/VERS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [IntField("anim_vers", 1)]

        return structure


# --- /BCS ------------------------------------------------------------------------------------
@dataclass
class Bcs(Keyword):
    """Defines boundary conditions on node groups for translational and rotational motion.
    Doc: (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/bcs_starter_r.htm)"""

    bcs_id: int
    bcs_title: str
    trarot: Sequence[Literal[0, 1]]
    skew_id: int
    grnd_id: int
    add_header: bool = True

    @property
    def keyword(self):
        return f"/BCS/{self.bcs_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("bcs_title", 1, 10),
            [
                BoolField("trarot", 1, 6, [4, 5, 6, 8, 9, 10]),
                IntField("skew_id", 2),
                IntField("grnd_id", 3),
            ],
        ]

        return structure


# --- /BCS/CYCLIC -----------------------------------------------------------------------------
@dataclass
class BcsCyclic(Keyword):
    """Defines a cyclic boundary condition on a structure in a fixed
    cylindrical coordinate system.
    Doc: (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/bcs_cyclic_starter_r.htm)
    """

    bcs_id: int
    bcs_cyclic_title: str
    grnd_id_1: int
    grnd_id_2: int
    skew_id: int = 0
    add_header: bool = True

    @property
    def keyword(self):
        return f"/BCS/{self.bcs_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("bcs_cyclic_title", 1, 10),
            [
                IntField("skew_id", 1),
                IntField("grnd_id_1", 2),
                IntField("grnd_id_2", 3),
            ],
        ]

        return structure


# --- /BCS/LAGMUL ------------------------------------------------------
@dataclass
class BcsLagmul(Keyword):
    """Defines boundary conditions on node groups using Lagrange multipliers.
    This keyword is not available for SPMD computation.
    Doc: (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/bcs_lagmul_starter_r.htm)
    """

    bcs_id: int
    bcs_title: str
    trarot: str
    skew_id: int
    grnd_id: int
    add_header: bool = True

    @property
    def keyword(self):
        return f"/BCS/{self.bcs_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("bcs_title", 1, 10),
            [
                BoolField("trarot", 1, 6, [4, 5, 6, 8, 9, 10]),
                IntField("skew_id", 2),
                IntField("grnd_id", 3),
            ],
        ]

        return structure


# --- /BEAM ------------------------------------------------------
@dataclass
class Beam(Keyword):
    """Describes the beam elements. Two properties (/PROP/TYPE3 (BEAM) and
    /PROP/TYPE18 (INT_BEAM)) are available for this beam element. The
    properties describing a beam element are all defined in a local beam
    coordinate system.
    Doc: (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/beam_starter_r.htm)
    """

    part_id: int
    beam_ids: List[int]
    node_ids: NDArray
    line00: str = "#/BEAM/part_ID\n"
    add_header: bool = True

    @property
    def keyword(self):
        return self.line00 + f"/BEAM/{self.part_id}"

    @property
    def pre_conditions(self):
        return [
            (
                len(self.beam_ids) == len(self.node_ids),
                "Pre-condition `len(beam_ids) == len(node_ids)` is violated.",
            )
        ]

    @property
    def structure(self):
        structure = []
        if len(self.node_ids[0]) == 2:
            structure.append(
                ArrayOfAtomicFields(
                    [
                        IntField("beam_ids", 1),
                        IntField("node_ids:ID_1|0", 2),
                        IntField("node_ids:ID_2|1", 3),
                    ]
                )
            )
        elif len(self.node_ids[0]) == 3:
            structure.append(
                ArrayOfAtomicFields(
                    [
                        IntField("beam_ids", 1),
                        IntField("node_ids:ID_1|0", 2),
                        IntField("node_ids:ID_2|1", 3),
                        IntField("node_ids:ID_3|2", 4),
                    ]
                )
            )

        return structure
