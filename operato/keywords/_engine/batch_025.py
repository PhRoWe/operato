#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /VEL/ROT                    /VEL/TRA                    /VERS
#


# --- /VEL/ROT ------------------------------------------------------
@dataclass
class VelRot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/VEL/ROT` is not implemented.")

    @property
    def keyword(self):
        return "/VEL/ROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /VEL/TRA ------------------------------------------------------
@dataclass
class VelTra(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/VEL/TRA` is not implemented.")

    @property
    def keyword(self):
        return "/VEL/TRA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /VERS ------------------------------------------------------
@dataclass
class Vers(Keyword):
    vers: int

    @property
    def keyword(self):
        return f"/VERS/{self.vers}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
