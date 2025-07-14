#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INIGRAV                    /INIMAP1D                   /INIMAP1D/FILE
# /INIMAP2D                   /INIMAP2D/FILE              /INIQUA
# /INIQUA/DENS                /INIQUA/ENER                /INIQUA/EPSP
#


# --- /INIGRAV ------------------------------------------------------
@dataclass
class Inigrav(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIGRAV` is not implemented.")

    @property
    def keyword(self):
        return "/INIGRAV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIMAP1D ------------------------------------------------------
@dataclass
class Inimap1d(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIMAP1D` is not implemented.")

    @property
    def keyword(self):
        return "/INIMAP1D"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIMAP1D/FILE ------------------------------------------------------
@dataclass
class Inimap1dFile(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIMAP1D/FILE` is not implemented.")

    @property
    def keyword(self):
        return "/INIMAP1D/FILE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIMAP2D ------------------------------------------------------
@dataclass
class Inimap2d(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIMAP2D` is not implemented.")

    @property
    def keyword(self):
        return "/INIMAP2D"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIMAP2D/FILE ------------------------------------------------------
@dataclass
class Inimap2dFile(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIMAP2D/FILE` is not implemented.")

    @property
    def keyword(self):
        return "/INIMAP2D/FILE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIQUA ------------------------------------------------------
@dataclass
class Iniqua(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIQUA` is not implemented.")

    @property
    def keyword(self):
        return "/INIQUA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIQUA/DENS ------------------------------------------------------
@dataclass
class IniquaDens(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIQUA/DENS` is not implemented.")

    @property
    def keyword(self):
        return "/INIQUA/DENS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIQUA/ENER ------------------------------------------------------
@dataclass
class IniquaEner(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIQUA/ENER` is not implemented.")

    @property
    def keyword(self):
        return "/INIQUA/ENER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIQUA/EPSP ------------------------------------------------------
@dataclass
class IniquaEpsp(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/INIQUA/EPSP` is not implemented.")

    @property
    def keyword(self):
        return "/INIQUA/EPSP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
