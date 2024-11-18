#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, KeywordCategory, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ABF                        /ADYREL                     /ALE/GRID/DISP
# /ALE/GRID/DONEA             /ALE/GRID/SPRING            /ALE/GRID/STANDARD
# /ALE/GRID/ZERO              /ALE/LINK/OFF               /ALE/LINK/ON
#


# --- /ABF ------------------------------------------------------
@dataclass
class Abf(Keyword):
    """Describes the output of .abf files. (.abf [binary] files are optimized
    for fast plotting of very large data sets and is intended for creating 2D
    and 3D plots using HyperGraph and HyperGraph 3D).
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/abf_engine_r.htm?zoom_highlight=abf)
    """

    dt_abf: float
    dt_t_w_abv: float

    @property
    def keyword(self):
        return "/ABF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [[FloatField("dt_abf", 1), FloatField("dt_t_w_abv", 3)]]

        return structure


# --- /ADYREL ------------------------------------------------------
@dataclass
class Adyrel(Keyword):
    """Dynamic relaxation with auto-defined adaptive damping.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/adyrel_engine_r.htm)"""

    t_start: float = 0.0
    t_stop: float | None = None

    @property
    def keyword(self):
        return "/ADYREL"

    @property
    def pre_conditions(self):
        if self.t_stop is None:
            return []

        return [
            (self.t_stop > self.t_start, "Pre-condition `t_stop > t_start` is violated")
        ]

    @property
    def structure(self):
        structure = [[FloatField("t_start", 1), FloatField("t_stop", 3)]]

        return structure


# --- /ALE/GRID/DISP ------------------------------------------------------
@dataclass
class AleGridDisp(Keyword):
    """The displacement of a grid node depends on the displacements of the neighboring grid nodes.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/ale_grid_disp_starter_r.htm)
    """

    u_max: float
    v_min: float

    @property
    def keyword(self):
        return "/ALE/GRID/DISP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [[FloatField("u_max", 1)], [FloatField("v_min", 1)]]

        return structure


# --- /ALE/GRID/DONEA ------------------------------------------------------
@dataclass
class AleGridDonea(Keyword):
    """With this keyword it is possible to modify grid formulation parameters, which
    initially were set in Starter keyword /ALE/GRID/DONEA.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/ale_grid_donea_engine_r.htm)
    """

    alpha: float
    gamma: float
    fscale_x: float
    fscale_y: float
    fscale_z: float
    v_min: float

    @property
    def keyword(self):
        return "/ALE/GRID/DONEA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        # We need to treat this keyword a little different because it has 6 float fields
        # on a single line. This is not allowed for starter keywords, but it is allowed
        # for engine keywords because the lines are free formatted.
        self.type = KeywordCategory.ENGINE

        structure = [
            [
                FloatField("alpha", 1),
                FloatField("gamma", 3),
                FloatField("fscale_x", 5),
                FloatField("fscale_y", 7),
                FloatField("fscale_z", 9),
                FloatField("v_min", 11),
            ]
        ]

        return structure


# --- /ALE/GRID/SPRING ------------------------------------------------------
@dataclass
class AleGridSpring(Keyword):
    """With this keyword it is possible to modify grid formulation parameters which
    initially be set in Starter keyword /ALE/GRID/SPRING.
      (Altair bar method for grid velocity computation).
      (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/ale_grid_spring_engine_r.htm)
    """

    Dt_0: float
    gamma: float
    eta: float
    nu: float
    v_min: float

    @property
    def keyword(self):
        return "/ALE/GRID/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):

        structure = [
            [
                FloatField("Dt_0", 1),
                FloatField("gamma", 3),
                FloatField("eta", 5),
                FloatField("nu", 7),
                FloatField("v_min", 9),
            ]
        ]

        return structure


# --- /ALE/GRID/STANDARD ------------------------------------------------------
@dataclass
class AleGridStandard(Keyword):
    """With this keyword it is possible to modify grid formulation parameters,
    which initially were set in Starter keyword /ALE/GRID/STANDARD.
    (Altair standard method for grid velocity computation). (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/ale_grid_standard_engine_r.htm)

    Args:
        Keyword (_type_): _description_

    Raises:
        NotImplementedError: _description_

    Returns:
        _type_: _description_
    """

    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/GRID/STANDARD` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/GRID/STANDARD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ALE/GRID/ZERO ------------------------------------------------------
@dataclass
class AleGridZero(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/GRID/ZERO` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/GRID/ZERO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ALE/LINK/OFF ------------------------------------------------------
@dataclass
class AleLinkOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/LINK/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/LINK/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ALE/LINK/ON ------------------------------------------------------
@dataclass
class AleLinkOn(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/ALE/LINK/ON` is not implemented.")

    @property
    def keyword(self):
        return "/ALE/LINK/ON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
