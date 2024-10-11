#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal, Sequence, Tuple, get_args

from numpy.typing import NDArray
from ..common import (
    ArrayOfAtomicFields,
    FloatField,
    IntField,
    Keyword,
    KeywordPreconditionsType,
    KeywordStructureType,
    MultiLineArrayOfAtomicFields,
    StringField,
    TextAlignment,
    VLSequenceOfAtomicField,
    check_if_all_values_are_present,
    get_literal_values,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SURF/SEG                   /SURF/SUBMODEL              /SURF/SUBSET
# /SURF/SURF                  /TABLE/0                    /TABLE/1
# /TETRA4                     /TETRA10                    /TH
#


# --- /SURF/SEG ------------------------------------------------------
@dataclass
class SurfSeg(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SEG` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SEG"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/SUBMODEL ------------------------------------------------------
@dataclass
class SurfSubmodel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SUBMODEL` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SUBMODEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/SUBSET ------------------------------------------------------
@dataclass
class SurfSubset(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SUBSET` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SUBSET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SURF/SURF ------------------------------------------------------
@dataclass
class SurfSurf(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/SURF/SURF` is not implemented.")

    @property
    def keyword(self):
        return "/SURF/SURF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TABLE/0 ------------------------------------------------------
@dataclass
class Table0(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TABLE/0` is not implemented.")

    @property
    def keyword(self):
        return "/TABLE/0"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TABLE/1 ------------------------------------------------------
@dataclass
class Table1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TABLE/1` is not implemented.")

    @property
    def keyword(self):
        return "/TABLE/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /TETRA4 ------------------------------------------------------
@dataclass
class Tetra4(Keyword):
    part_id: int
    tetra_ids: List[int] | NDArray
    node_ids: List[Tuple[int, ...]] | NDArray
    line00: str = "#/TETRA4/part_ID\n"
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#tetra_id|-node_id1|-node_id2|-node_id3|-node_id4|----6----|----7----|----8----|----9----|----10---|"
    )

    @property
    def keyword(self):
        return f"/TETRA4/{self.part_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("line1", 1, 10),
            ArrayOfAtomicFields(
                [
                    IntField("tetra_ids", 1),
                    IntField("node_ids:ID_1|0", 2),
                    IntField("node_ids:ID_2|1", 3),
                    IntField("node_ids:ID_3|2", 4),
                    IntField("node_ids:ID_4|3", 5),
                ]
            ),
        ]

        return structure


# --- /TETRA10 ------------------------------------------------------
@dataclass
class Tetra10(Keyword):
    part_id: int
    tetra_ids: List[int] | NDArray
    node_ids: List[Tuple[int, ...]] | NDArray
    line00: str = "#/TETRA10/part_ID\n"

    @property
    def keyword(self):
        return f"/TETRA10/{self.part_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = [
            MultiLineArrayOfAtomicFields(
                [
                    ArrayOfAtomicFields([IntField("tetra_ids", 1)]),
                    ArrayOfAtomicFields(
                        [
                            IntField("node_ids:ID_1|0", 1),
                            IntField("node_ids:ID_2|1", 2),
                            IntField("node_ids:ID_3|2", 3),
                            IntField("node_ids:ID_4|3", 4),
                            IntField("node_ids:ID_5|4", 5),
                            IntField("node_ids:ID_6|5", 6),
                            IntField("node_ids:ID_7|6", 7),
                            IntField("node_ids:ID_8|7", 8),
                            IntField("node_ids:ID_9|8", 9),
                            IntField("node_ids:ID_10|9", 10),
                        ]
                    ),
                ]
            ),
        ]

        return structure


# --- /TH ------------------------------------------------------
@dataclass
class Th(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/TH` is not implemented.")

    @property
    def keyword(self):
        return "/TH"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
