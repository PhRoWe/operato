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
    ArrayOfAtomicFields,
    KeywordStructureType,
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
    """https://help.altair.com/hwsolvers/rad/topics/solvers/rad/anim_brick_tens_engine_r.htm
    Args:
        keyword1: (Literal): Definition of requested tens. STRESS for Stress tensor. STRAIN for Strain tensor. EPSP for
            Plastic strain tensor at integration points, only available for /MAT/LAW24 with Icpre=2.
        keyword2:(str):  Possible settings: 0 or blank for Mean value in brick element. "ijk" for value in integration
            Point of brick element where i is Integration point number in direction r. j is Integration point number in direction s.
            k is integration point number in direction t. "ALL" for values in all the integration points of brick element.
    """

    keyword1: Literal["STRESS", "STRAIN", "EPSP"]
    keyword2: str | None = None

    @property
    def keyword(self):
        if self.keyword2 is None:
            return f"/ANIM/BRICK/TENS/{self.keyword1}"
        else:
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

    # TODO: Implementation

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

    # TODO: Implementation

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
    """Write animation files (A-files) at a time frequency equal to Tfreq, the first
    file being written at time Tstart. The animation file name will be RunnameAnnn
    where Runname is the Run Name and nnn is the file number.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/anim_dt_engine_r.htm)"""

    t_start: float
    t_freq: float
    t_stop: float | None = None
    # added line for readability
    line0: str = (
        "#-----------T_start|-------------T_freq|------------T-stop-|----7----|----8----|----9----|----10---|"
    )

    @property
    def keyword(self):
        return "/ANIM/DT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("line0", 1, 10),
            [
                FloatField("t_start", 1),
                FloatField("t_freq", 3),
                FloatField("t_stop", 5),
            ],
        ]

        return structure


# --- /ANIM/Eltyp/FORC ------------------------------------------------------
@dataclass
class AnimEltypForc(Keyword):
    eltype: str

    @property
    def keyword(self):
        return f"/ANIM/{self.eltype}/FORC"

    @property
    def pre_conditions(self):
        return (self.restype in ["BEAM", "SPRING", "TRUS"], "Unknown response type.")

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/Eltyp/Restype ------------------------------------------------------
@dataclass
class AnimEltypRestype(Keyword):
    eltype: str
    restype: str

    @property
    def keyword(self):
        return f"/ANIM/{self.eltype}/{self.restype}"

    @property
    def pre_conditions(self):
        restype_pos = [
            "AMS",
            "DAM1",
            "DAM2",
            "DAM3",
            "DENS",
            "DT",
            "ENER",
            "EPSD",
            "EPSP",
            "ESPN/N",
            "ESPN/All",
            "EPSX",
            "HOURG",
            "P",
            "SIGX",
            "SIGY",
            "SIGZ",
            "SIGXY",
            "SIGYZ",
            "SIGZX",
            "TEMP",
            "THIC",
            "TILLOTSON",
            "USRi",
            "VONM",
            "MACH",
            "OFF",
            "DAMG",
            "EPSX",
        ]
        return [
            (
                self.eltype in ["ELEM", "BEAM", "SPRING", "TRUS"],
                "Unknown element type specified.",
            ),
            (self.restype in restype_pos, "Unknown response type."),
        ]

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/Eltyp/TDET ------------------------------------------------------
@dataclass
class AnimEltypTdet(Keyword):
    attr1: int
    attr2: float

    # TODO: Implementation

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
    """Generates animation files containing averaged grip point strain data calculated
    by bilinear extrapolation using shape functions from the integration point results.
    The average value at each node is calculated by each element which connected to
    this node.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/anim_gps_strain_tens_engine_r.htm)

    """

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
    """Generates animation files containing averaged grip point stress data calculated
    by bilinear extrapolation using shape functions from the integration point results.
    The average value at each node is calculated by each element which connected to
    this node.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/anim_gps_tens_engine_r.htm)
    """

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
