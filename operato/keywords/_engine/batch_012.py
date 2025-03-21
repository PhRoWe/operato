#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal
from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    ArrayOfAtomicFields,
    VLSequenceOfAtomicField,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /H3D/SOLID                  /H3D/SPH                    /H3D/SPRING
# /H3D/TITLE                  /H3D/TRUSS                  /IMPL/AUTOSPC
# /IMPL/BUCKL/1               /IMPL/BUCKL/2               /IMPL/CHECK
#


# --- /H3D/SOLID ------------------------------------------------------
@dataclass
class H3dSolid(Keyword):
    key3: str
    key4: None | str = None
    key5: None | str = None
    part_id: None | List[int] = None

    @property
    def keyword(self):
        if self.key4 is not None and self.key5 is not None:
            return f"/H3D/SOLID/{self.key3}/{self.key4}/{self.key5}"
        elif self.key4 is not None and self.key5 is None:
            return f"/H3D/SOLID/{self.key3}/{self.key4}"
        elif self.key4 is None and self.key5 is None:
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


# --- /H3D/SPH ------------------------------------------------------
@dataclass
class H3dSph(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/H3D/SPH` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/SPH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /H3D/SPRING ------------------------------------------------------
@dataclass
class H3dSpring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/H3D/SPRING` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /H3D/TITLE ------------------------------------------------------
@dataclass
class H3dTitle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/H3D/TITLE` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/TITLE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /H3D/TRUSS ------------------------------------------------------
@dataclass
class H3dTruss(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/H3D/TRUSS` is not implemented.")

    @property
    def keyword(self):
        return "/H3D/TRUSS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/AUTOSPC ------------------------------------------------------
@dataclass
class ImplAutospc(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/AUTOSPC` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/AUTOSPC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/BUCKL/1 ------------------------------------------------------
@dataclass
class ImplBuckl1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/BUCKL/1` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/BUCKL/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/BUCKL/2 ------------------------------------------------------
@dataclass
class ImplBuckl2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/BUCKL/2` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/BUCKL/2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/CHECK ------------------------------------------------------
@dataclass
class ImplCheck(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/CHECK` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/CHECK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
