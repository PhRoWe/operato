#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPL/DIVERG/n              /IMPL/DT/1                  /IMPL/DT/2
# /IMPL/DT/3                  /IMPL/DT/FIXPOINT           /IMPL/DT/STOP
# /IMPL/DTINI                 /IMPL/DYNA/1                /IMPL/DYNA/2
#


# --- /IMPL/DIVERG/n ------------------------------------------------------
@dataclass
class ImplDivergN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/DIVERG/n` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DIVERG/n"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/DT/1 ------------------------------------------------------
@dataclass
class ImplDt1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/DT/1` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/DT/2 ------------------------------------------------------
@dataclass
class ImplDt2(Keyword):
    """Implicit automatic time step control method 2 (Arc-length).This method is
    preferred for general nonlinear implicit analysis.
    Arc-length method is used to accelerate and to control the convergence.
    The time step is determined by displacement norm control (arc-length).
    (https://2022.help.altair.com/2022.2/hwsolvers/rad/topics/solvers/rad/impl_dt_2_engine_r.htm)
    """

    it_w: int
    l_arc: float
    l_dtn: int
    dt_scad: float
    dt_scamax: float
    # added commentary line for readability of input deck
    line: str = (
        "#--- it_w|--------------l_arc|----L_dtn|------------dt_scad|----------dt_scamax|----9----|----10---|"
    )

    @property
    def keyword(self):
        return "/IMPL/DT/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("line", 1, 10),
            [
                IntField("it_w", 1),
                FloatField("l_arc", 2),
                IntField("l_dtn", 4),
                FloatField("dt_scad", 5),
                FloatField("dt_scamax", 7),
            ],
        ]

        return structure


# --- /IMPL/DT/3 ------------------------------------------------------
@dataclass
class ImplDt3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/DT/3` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/DT/FIXPOINT ------------------------------------------------------
@dataclass
class ImplDtFixpoint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/DT/FIXPOINT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/FIXPOINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/DT/STOP ------------------------------------------------------
@dataclass
class ImplDtStop(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/DT/STOP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DT/STOP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/DTINI ------------------------------------------------------
@dataclass
class ImplDtini(Keyword):
    """Initial time step for nonlinear implicit analysis.
    Initial time step determines initial loading increment in this run session.
    This key should be defined in nonlinear analysis.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/impl_dtini_engine_r.htm)
    """

    dt: float
    """Initial implicit time step"""

    @property
    def keyword(self):
        return "/IMPL/DTINI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [FloatField("dt", 1)]

        return structure


# --- /IMPL/DYNA/1 ------------------------------------------------------
@dataclass
class ImplDyna1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/DYNA/1` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DYNA/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/DYNA/2 ------------------------------------------------------
@dataclass
class ImplDyna2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/DYNA/2` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/DYNA/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
