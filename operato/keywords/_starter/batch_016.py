#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import (
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
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/GRSHEL` is not implemented.")

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
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/GRSPRI` is not implemented.")

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
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/GRTRIA` is not implemented.")

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
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/GRTRUS` is not implemented.")

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
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/HEAT/MAT` is not implemented.")

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
    add_header: bool = True

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
    add_header: bool = True

    @property
    def keyword(self):
        line = f"/IMPDISP/{self.impdisp_id}"
        if self.unit_id is not None:
            line += f"/{self.unit_id}"
        return line

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("title", 1, 10),
            [
                IntField("fct_id_t", 1),
                StringField("dir", 2, 1, alignment=TextAlignment.CENTER),
                IntField("skew_id", 3),
                IntField("sens_id", 4),
                IntField("grnd_id", 5),
                IntField("icoor", 7),
            ],
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
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPDISP/FGEO` is not implemented.")

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
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPFLUX` is not implemented.")

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
