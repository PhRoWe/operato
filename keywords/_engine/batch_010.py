#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal
from ..common import FloatField, IntField, Keyword, StringField, VLSequenceOfAtomicField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /DYNAIN/SHELL/STRESS/FULL   /DYREL                      /DYREL/1
# /END/ENGINE                 /FUNCT                      /FVMBAG/MODIF
# /FXINP                      /H3D/BEAM                   /H3D/COMPRESS
#


# --- /DYNAIN/SHELL/STRESS/FULL ------------------------------------------------------
@dataclass
class DynainShellStressFull(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError(
            "Keyword `/DYNAIN/SHELL/STRESS/FULL` is not implemented."
        )

    @property
    def keyword(self):
        return "/DYNAIN/SHELL/STRESS/FULL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DYREL ------------------------------------------------------
@dataclass
class Dyrel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DYREL` is not implemented.")

    @property
    def keyword(self):
        return "/DYREL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DYREL/1 ------------------------------------------------------
@dataclass
class Dyrel1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DYREL/1` is not implemented.")

    @property
    def keyword(self):
        return "/DYREL/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /END/ENGINE ------------------------------------------------------
@dataclass
class EndEngine(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/END/ENGINE` is not implemented.")

    @property
    def keyword(self):
        return "/END/ENGINE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FUNCT ------------------------------------------------------
@dataclass
class Funct(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FUNCT` is not implemented.")

    @property
    def keyword(self):
        return "/FUNCT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FVMBAG/MODIF ------------------------------------------------------
@dataclass
class FvmbagModif(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FVMBAG/MODIF` is not implemented.")

    @property
    def keyword(self):
        return "/FVMBAG/MODIF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FXINP ------------------------------------------------------
@dataclass
class Fxinp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FXINP` is not implemented.")

    @property
    def keyword(self):
        return "/FXINP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /H3D/BEAM ------------------------------------------------------
@dataclass
class H3dBeam(Keyword):
    key3: str
    key4: None | str = None
    part_id: None | List[int] = None

    @property
    def keyword(self):
        if self.key4 is not None:
            return f"/H3D/Beam/{self.key3}/{self.key4}"
        elif self.key4 is None:
            return f"/H3D/SOLID/{self.key3}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []
        if self.part_id is not None:
            structure = [
                VLSequenceOfAtomicField(
                    IntField("part_id", 1),
                )
            ]
        return structure


# --- /H3D/COMPRESS ------------------------------------------------------
@dataclass
class H3dCompress(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/H3D/COMPRESS` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/COMPRESS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
