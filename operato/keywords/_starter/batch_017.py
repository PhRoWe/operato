#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPLICIT                   /IMPTEMP                    /IMPVEL
# /IMPVEL/FGEO                /IMPVEL/LAGMUL              /INIBEAM/AUX
# /INIBEAM/FULL               /INIBRI                     /INICRACK
#


# --- /IMPLICIT ------------------------------------------------------
@dataclass
class Implicit(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPLICIT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPLICIT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPTEMP ------------------------------------------------------
@dataclass
class Imptemp(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPTEMP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPTEMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPVEL ------------------------------------------------------
@dataclass
class Impvel(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPVEL` is not implemented.")

    @property
    def keyword(self):
        return "/IMPVEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPVEL/FGEO ------------------------------------------------------
@dataclass
class ImpvelFgeo(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPVEL/FGEO` is not implemented.")

    @property
    def keyword(self):
        return "/IMPVEL/FGEO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPVEL/LAGMUL ------------------------------------------------------
@dataclass
class ImpvelLagmul(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPVEL/LAGMUL` is not implemented.")

    @property
    def keyword(self):
        return "/IMPVEL/LAGMUL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- #include ------------------------------------------------------
@dataclass
class Include(Keyword):
    filename: str
    add_header: bool = False

    @property
    def keyword(self):
        return f"#include {self.filename}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIBEAM/AUX ------------------------------------------------------
@dataclass
class InibeamAux(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIBEAM/AUX` is not implemented.")

    @property
    def keyword(self):
        return "/INIBEAM/AUX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIBEAM/FULL ------------------------------------------------------
@dataclass
class InibeamFull(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIBEAM/FULL` is not implemented.")

    @property
    def keyword(self):
        return "/INIBEAM/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIBRI ------------------------------------------------------
@dataclass
class Inibri(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIBRI` is not implemented.")

    @property
    def keyword(self):
        return "/INIBRI"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INICRACK ------------------------------------------------------
@dataclass
class Inicrack(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/INICRACK` is not implemented.")

    @property
    def keyword(self):
        return "/INICRACK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
