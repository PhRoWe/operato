#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /EBCS/INIV                  /EBCS/INLET                 /EBCS/MONVOL
# /EBCS/NORMV                 /EBCS/NRF                   /EBCS/PRES
# /EBCS/VALVIN                /EBCS/VALVOUT               /EBCS/VEL
#


# --- /EBCS/INIV ------------------------------------------------------
@dataclass
class EbcsIniv(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/INIV` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/INIV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/INLET ------------------------------------------------------
@dataclass
class EbcsInlet(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/INLET` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/INLET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/MONVOL ------------------------------------------------------
@dataclass
class EbcsMonvol(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/MONVOL` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/MONVOL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/NORMV ------------------------------------------------------
@dataclass
class EbcsNormv(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/NORMV` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/NORMV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/NRF ------------------------------------------------------
@dataclass
class EbcsNrf(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/NRF` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/NRF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/PRES ------------------------------------------------------
@dataclass
class EbcsPres(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/PRES` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/PRES"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/VALVIN ------------------------------------------------------
@dataclass
class EbcsValvin(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/VALVIN` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/VALVIN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/VALVOUT ------------------------------------------------------
@dataclass
class EbcsValvout(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EBCS/VALVOUT` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/VALVOUT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EBCS/VEL ------------------------------------------------------
@dataclass
class EbcsVel(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/EBCS/VEL` is not implemented.")

    @property
    def keyword(self):
        return "/EBCS/VEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
