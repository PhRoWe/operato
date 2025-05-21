#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    ArrayOfAtomicFields,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /FRAME/MOV2                 /FRAME/NOD                  /FRIC_ORIENT
# /FRICTION                   /FUNC_2D                    /FUNCT
# /FUNCT_SMOOTH               /FXBODY                     /GAUGE
#


# --- /FRAME/MOV2 ------------------------------------------------------
@dataclass
class FrameMov2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/FRAME/MOV2` is not implemented.")

    @property
    def keyword(self):
        return "/FRAME/MOV2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FRAME/NOD ------------------------------------------------------
@dataclass
class FrameNod(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/FRAME/NOD` is not implemented.")

    @property
    def keyword(self):
        return "/FRAME/NOD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FRIC_ORIENT ------------------------------------------------------
@dataclass
class FricOrient(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/FRIC_ORIENT` is not implemented.")

    @property
    def keyword(self):
        return "/FRIC_ORIENT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FRICTION ------------------------------------------------------
@dataclass
class Friction(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/FRICTION` is not implemented.")

    @property
    def keyword(self):
        return "/FRICTION"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FUNC_2D ------------------------------------------------------
@dataclass
class Func2d(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/FUNC_2D` is not implemented.")

    @property
    def keyword(self):
        return "/FUNC_2D"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FUNCT ------------------------------------------------------
@dataclass
class Funct(Keyword):
    fct_id: int
    fct_title: str
    x: float | List[float]
    y: float | List[float]
    # added commentary lines for readability
    line1: str = "#                  X                   Y"
    add_separator: bool = True

    @property
    def keyword(self):
        return f"/FUNCT/{self.fct_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("fct_title", 1, 3),
            StringField("line1", 1, 10),
            ArrayOfAtomicFields([FloatField("x", 1), FloatField("y", 3)]),
        ]

        return structure


# --- /FUNCT_SMOOTH ------------------------------------------------------
@dataclass
class FunctSmooth(Keyword):
    """Defines a smoothstep analytic function to be used with loads.
    https://help.altair.com/hwsolvers/rad/topics/solvers/rad/funct_smooth_starter_r.htm
    """

    fct_id: int
    fct_title: str
    x: List[float]
    y: List[float]
    Ascalex: float = 1.0
    Fscaley: float = 1.0
    Ashiftx: float = 0.0
    Fshifty: float = 0.0

    # added commentary lines for readability
    line0: str = "#/FUNCT_SMOOTH/fct_ID\n"
    line1: str = (
        "#-----------Ascalex|------------Fscaley|------------Ashiftx|------------Fshifty|----9----|----10---|"
    )
    line2: str = "#                  X                   Y"
    add_separator: bool = True

    @property
    def keyword(self):
        return self.line0 + f"/FUNCT_SMOOTH/{self.fct_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("fct_title", 1, 3),
            StringField("line1", 1, 10),
            [
                FloatField("Ascalex", 1),
                FloatField("Fscaley", 3),
                FloatField("Ashiftx", 5),
                FloatField("Fshifty", 7),
            ],
            StringField("line2", 1, 10),
            ArrayOfAtomicFields([FloatField("x", 1), FloatField("y", 3)]),
        ]

        return structure


# --- /FXBODY ------------------------------------------------------
@dataclass
class Fxbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/FXBODY` is not implemented.")

    @property
    def keyword(self):
        return "/FXBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GAUGE ------------------------------------------------------
@dataclass
class Gauge(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/GAUGE` is not implemented.")

    @property
    def keyword(self):
        return "/GAUGE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
