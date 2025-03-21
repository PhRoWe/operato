#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    ArrayOfAtomicFields,
    VLSequenceOfAtomicField,
)
from typing import List

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SURF/ELLIPS                /SURF/GRBRIC/EXT            /SURF/GRBRIC/FREE
# /SURF/GRSH3N                /SURF/GRSHEL                /SURF/MAT
# /SURF/PART                  /SURF/PLANE                 /SURF/PROP
#


# --- /SURF/ELLIPS ------------------------------------------------------
@dataclass
class SurfEllips(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/ELLIPS` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/ELLIPS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/GRBRIC/EXT ------------------------------------------------------
@dataclass
class SurfGrbricExt(Keyword):
    surf_id: int
    item_ids: List[int]
    surf_title: str | None = "Standard"
    unit_id: int | int = None

    # added commentary lines for readability of deck
    line00: str = "#/SURF/GRBRIC/EXT/surf_ID/unit_ID\n"
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#item_id1|-item_id2|-item_id3|-item_id4|-item_id5|-item_id6|-item_id7|-item_id8|-item_id9|item_id10|"
    )

    @property
    def keyword(self):
        if self.unit_id is None:
            return self.line00 + f"/SURF/GRBRIC/EXT/{self.surf_id}"
        else:
            return self.line00 + f"/SURF/GRBRIC/EXT/{self.surf_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [StringField("surf_title", 1, 10), StringField("line1", 1, 10)]
        if type(self.item_ids) == int:
            structure.append(IntField("item_ids", 1))
        else:
            structure.append(VLSequenceOfAtomicField(IntField("item_ids", 1)))

        return structure


# --- /SURF/GRBRIC/FREE ------------------------------------------------------
@dataclass
class SurfGrbricFree(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/GRBRIC/FREE` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/GRBRIC/FREE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/GRSH3N ------------------------------------------------------
@dataclass
class SurfGrsh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/GRSH3N` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/GRSH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/GRSHEL ------------------------------------------------------
@dataclass
class SurfGrshel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/GRSHEL` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/GRSHEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/MAT ------------------------------------------------------
@dataclass
class SurfMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/PART ------------------------------------------------------
@dataclass
class SurfPart(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/PART` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/PART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/PLANE ------------------------------------------------------
@dataclass
class SurfPlane(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/PLANE` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/PLANE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/PROP ------------------------------------------------------
@dataclass
class SurfProp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SURF/PROP` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/PROP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
