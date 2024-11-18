#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /STATE/SPRING/FULL          /STATE/STR_FILE             /STATE/TRUSS/FULL
# /STOP                       /STOP/LSENSOR               /TFILE
# /TH/VERS                    /THERMAL                    /TITLE
#


# --- /STATE/SPRING/FULL ------------------------------------------------------
@dataclass
class StateSpringFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/STATE/SPRING/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/SPRING/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /STATE/STR_FILE ------------------------------------------------------
@dataclass
class StateStrFile(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/STATE/STR_FILE` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/STR_FILE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /STATE/TRUSS/FULL ------------------------------------------------------
@dataclass
class StateTrussFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/STATE/TRUSS/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/STATE/TRUSS/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /STOP ------------------------------------------------------
@dataclass
class Stop(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/STOP` is not implemented.")

    @property
    def keyword(self):
        return "/STOP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /STOP/LSENSOR ------------------------------------------------------
@dataclass
class StopLsensor(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/STOP/LSENSOR` is not implemented.")

    @property
    def keyword(self):
        return "/STOP/LSENSOR"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TFILE ------------------------------------------------------
@dataclass
class Tfile(Keyword):
    """Defines the frequency of writing the time history file of T-file "RunnameTnn".
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/tfile_engine_r.htm)
    """

    dt_his: float
    _type: int = 4

    @property
    def keyword(self):
        return f"/TFILE/{self._type}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [FloatField("dt_his", 1)]

        return structure


# --- /TH/VERS ------------------------------------------------------
@dataclass
class ThVers(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/TH/VERS` is not implemented.")

    @property
    def keyword(self):
        return "/TH/VERS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /THERMAL ------------------------------------------------------
@dataclass
class Thermal(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/THERMAL` is not implemented.")

    @property
    def keyword(self):
        return "/THERMAL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TITLE ------------------------------------------------------
@dataclass
class Title(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/TITLE` is not implemented.")

    @property
    def keyword(self):
        return "/TITLE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
