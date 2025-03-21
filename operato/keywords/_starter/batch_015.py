#!/usr/bin/env python3

from dataclasses import dataclass
from math import ceil
from typing import List
from numpy.typing import NDArray

from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    ArrayOfAtomicFields,
    VLSequenceOfAtomicField,
    KeywordStructureType,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /GAUGE/SPH                  /GJOINT                     /GRAV
# /GRBEAM                     /GRBRIC                     /GRNOD
# /GRPART                     /GRQUAD                     /GRSH3N
#


# --- /GAUGE/SPH ------------------------------------------------------
@dataclass
class GaugeSph(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GAUGE/SPH` is not implemented.")

    @property
    def keyword(self):
        return "/GAUGE/SPH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GJOINT ------------------------------------------------------
@dataclass
class Gjoint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GJOINT` is not implemented.")

    @property
    def keyword(self):
        return "/GJOINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRAV ------------------------------------------------------
@dataclass
class Grav(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GRAV` is not implemented.")

    @property
    def keyword(self):
        return "/GRAV"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRBEAM ------------------------------------------------------
@dataclass
class Grbeam(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/GRBEAM` is not implemented.")

    @property
    def keyword(self):
        return "/GRBEAM"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRBRIC ------------------------------------------------------
@dataclass
class Grbric(Keyword):
    grbric_id: int

    @property
    def keyword(self):
        return "/GRBRIC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRBRICBRIC ------------------------------------------------------
@dataclass
class GrbricBric(Keyword):
    grbric_id: int
    item_ids: List[int]
    unit_id: int | None = int
    grbric_title: str | None = "Standard"
    # added commentary lines for readability of deck
    line00: str = "#/GRBRIC/BRIC/grbric_ID/unit_ID\n"
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#item_id1|-item_id2|-item_id3|-item_id4|-item_id5|-item_id6|-item_id7|-item_id8|-item_id9|item_id10|"
    )

    @property
    def keyword(self):
        if self.unit_id is None:
            return self.line00 + f"/GRBRIC/BRIC/{self.grbric_id}"
        else:
            return self.line00 + f"/GRBRIC/BRIC/{self.grbric_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [StringField("grbric_title", 1, 10), StringField("line1", 1, 10)]
        if type(self.item_ids) == int:
            structure.append(IntField("item_ids", 1))
        else:
            structure.append(VLSequenceOfAtomicField(IntField("item_ids", 1)))

        return structure


# --- /GRNOD ------------------------------------------------------
@dataclass
class Grnod(Keyword):
    grnd_id: int

    @property
    def keyword(self):
        return "/GRNOD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRNOD/NODE --------------------------------------------------
@dataclass
class GrnodNode(Grnod):
    grnd_title: str
    item_ids: List[int]
    unit_id: int | None = None
    line00: str = "#/GRNOD/NODE/grnd_ID/unit_ID\n"

    @property
    def keyword(self):
        if self.unit_id is not None:
            return self.line00 + f"/GRNOD/NODE/{self.grnd_id}/{self.unit_id}"
        else:
            return self.line00 + f"/GRNOD/NODE/{self.grnd_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        if type(self.item_ids) == int:
            structure: KeywordStructureType = [
                StringField("grnd_title", 1, 3),
                IntField("item_ids", 1),
            ]
        else:
            structure: KeywordStructureType = [
                StringField("grnd_title", 1, 3),
                VLSequenceOfAtomicField(IntField("item_ids", 1)),
            ]

        return structure


# --- /GRPART ------------------------------------------------------
@dataclass
class GrpartPart(Keyword):
    grprt_id: int
    grprt_title: str
    item_ids: List[int]
    line00: str = "#/GRPART/PART/grprt_ID\n"

    @property
    def keyword(self):
        return self.line00 + f"/GRNOD/NODE/{self.grnd_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        if type(self.item_ids) == int:
            structure: KeywordStructureType = [
                StringField("grprt_title", 1, 3),
                IntField("item_ids", 1),
            ]
        else:
            structure: KeywordStructureType = [
                StringField("grprt_title", 1, 3),
                VLSequenceOfAtomicField(IntField("item_ids", 1)),
            ]

        return structure


# --- /GRPARTPART ------------------------------------------------------
@dataclass
class GrpartPartPart(Keyword):
    grpart_id: int
    grpart_title: str

    @property
    def keyword(self):
        return "/GRPART"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRQUAD ------------------------------------------------------
@dataclass
class Grquad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GRQUAD` is not implemented.")

    @property
    def keyword(self):
        return "/GRQUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /GRQUAD_QUAD ------------------------------------------------------
@dataclass
class Grquadquad(Keyword):
    grquad_id: int
    item_ids: List[int]
    unit_id: int | None = None
    grquad_title: str | None = None

    @property
    def keyword(self):
        if self.unit_id == None:
            return f"/GRQUAD/{self.grquad_id}"
        elif self.unit_id != None:
            return f"/GRQUAD/{self.grquad_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("grquad_title", 1, 3),
            VLSequenceOfAtomicField(IntField("item_ids", 1)),
        ]

        return structure


# --- /GRSH3N ------------------------------------------------------
@dataclass
class Grsh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/GRSH3N` is not implemented.")

    @property
    def keyword(self):
        return "/GRSH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
