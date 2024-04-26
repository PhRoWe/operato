#!/usr/bin/env python3

from dataclasses import dataclass
from typing import Literal
from ..common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    VLSequenceOfAtomicField,
    get_literal_values,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ANIM/BRICK/TENS            /ANIM/BRICK/TENS/DAMA       /ANIM/BRICK/VDAMi
# /ANIM/DT                    /ANIM/Eltyp/FORC            /ANIM/Eltyp/Restype
# /ANIM/Eltyp/TDET            /ANIM/GPS/STRAIN/TENS       /ANIM/GPS/STRESS/TENS
#


# --- /ANIM/BRICK/TENS ------------------------------------------------------
@dataclass
class AnimBrickTens(Keyword):
    keyword1: Literal["STRESS", "STRAIN", "EPSP"]
    keyword2: str

    @property
    def keyword(self):
        return f"/ANIM/BRICK/TENS/{self.keyword1}/{self.keyword2}"

    @property
    def pre_conditions(self):
        return [
            (
                self.keyword1 in get_literal_values(self, "keyword1"),
                f"Invalid `keyword1` specifier -> {self.keyword1}",
            )
        ]

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/BRICK/TENS/DAMA ------------------------------------------------------
@dataclass
class AnimBrickTensDama(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/BRICK/TENS/DAMA` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/BRICK/TENS/DAMA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/BRICK/VDAMi ------------------------------------------------------
@dataclass
class AnimBrickVdami(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/BRICK/VDAMi` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/BRICK/VDAMi"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/DT ------------------------------------------------------
@dataclass
class AnimDt(Keyword):
    t_start: float
    t_freq: float
    t_stop: float = 1e20
    # added line for readability
    line1 = str = "#    TSTART     TFREQ     TSTOP"

    @property
    def keyword(self):
        return "/ANIM/DT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            FloatField("t_start", 1),
            FloatField("t_freq", 2),
            FloatField("t_stop", 3),
        ]

        return structure


# --- /ANIM/Eltyp/FORC ------------------------------------------------------
@dataclass
class AnimEltypForc(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/Eltyp/FORC` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/Eltyp/FORC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/Eltyp/Restype ------------------------------------------------------
@dataclass
class AnimEltypRestype(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/Eltyp/Restype` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/Eltyp/Restype"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/Eltyp/TDET ------------------------------------------------------
@dataclass
class AnimEltypTdet(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/Eltyp/TDET` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/Eltyp/TDET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/GPS/STRAIN/TENS ------------------------------------------------------
@dataclass
class AnimGpsStrainTens(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/GPS/STRAIN/TENS` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/GPS/STRAIN/TENS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/GPS/STRESS/TENS ------------------------------------------------------
@dataclass
class AnimGpsStressTens(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ANIM/GPS/STRESS/TENS` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/GPS/STRESS/TENS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
