#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    KeywordStructureType,
    TextAlignment,
)
from typing import Literal

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /GRSHEL                     /GRSPRI                     /GRTRIA
# /GRTRUS                     /HEAT/MAT                   /IMPACC
# /IMPDISP                    /IMPDISP/FGEO               /IMPFLUX
#


# --- /GRSHEL ------------------------------------------------------
@dataclass
class Grshel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GRSHEL` is not implemented.")

    @property
    def keyword(self):
        return "/GRSHEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRSPRI ------------------------------------------------------
@dataclass
class Grspri(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GRSPRI` is not implemented.")

    @property
    def keyword(self):
        return "/GRSPRI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRTRIA ------------------------------------------------------
@dataclass
class Grtria(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GRTRIA` is not implemented.")

    @property
    def keyword(self):
        return "/GRTRIA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRTRUS ------------------------------------------------------
@dataclass
class Grtrus(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GRTRUS` is not implemented.")

    @property
    def keyword(self):
        return "/GRTRUS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /HEAT/MAT ------------------------------------------------------
@dataclass
class HeatMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/HEAT/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/HEAT/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPACC ------------------------------------------------------
@dataclass
class Impacc(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPACC` is not implemented.")

    @property
    def keyword(self):
        return "/IMPACC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPDISP ------------------------------------------------------
@dataclass
class Impdisp(Keyword):
    impdisp_id: int
    fct_id_t: int
    dir: Literal[
        "X",
        "Y",
        "Z",
        "XY",
        "XZ",
        "YZ",
        "XYZ",
        "XX",
        "YY",
        "ZZ",
        "XXYY",
        "XXZZ",
        "YYZZ",
        "XXYYZZ",
    ]
    skew_id: int
    sens_id: int
    grnd_id: int
    t_start: float
    t_stop: float | None = None
    icoor: int | None = 0
    """defaults to 0 (cartesian coordinates)"""
    unit_id: int | None = None
    title: str | None = ""
    a_scale_x: float | None = None
    f_scale_y: float | None = None

    # added commentary lines for readability of deck
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#--Fct_ID|------Dir|--skew_ID|--sens_ID|--grnd_ID|----6----|----icoor|----8----|----9----|----10---|"
    )
    line2: str = (
        "#----------Ascale_x|-----------Fscale_y|------------T_start|-------------T_stop|----9----|----10---|"
    )

    @property
    def keyword(self):
        return "/IMPDISP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("title", 1, 10),
            StringField("line1", 1, 10),
            [
                IntField("fct_id_t", 1),
                StringField("dir", 2, 1, alignment=TextAlignment.CENTER),
                IntField("skew_id", 3),
                IntField("sens_id", 4),
                IntField("grnd_id", 5),
                IntField("icoor", 7),
            ],
            StringField("line2", 1, 10),
            [
                FloatField("a_scale_x", 1),
                FloatField("f_scale_y", 3),
                FloatField("t_start", 5),
                FloatField("t_stop", 7),
            ],
        ]

        return structure


# --- /IMPDISP/FGEO ------------------------------------------------------
@dataclass
class ImpdispFgeo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPDISP/FGEO` is not implemented.")

    @property
    def keyword(self):
        return "/IMPDISP/FGEO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPFLUX ------------------------------------------------------
@dataclass
class Impflux(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPFLUX` is not implemented.")

    @property
    def keyword(self):
        return "/IMPFLUX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
