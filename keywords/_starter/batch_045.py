#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal, Sequence, Tuple, get_args

from numpy.typing import NDArray

from ..common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    ArrayOfAtomicFields,
    KeywordStructureType,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PROP/TYPE35                /PROP/TYPE36                /PROP/TYPE43
# /PROP/TYPE44                /PROP/TYPE45                /PROP/TYPE46
# /PROP/TYPE51                /QUAD                       /RADIATION
#


# --- /PROP/TYPE35 ------------------------------------------------------
@dataclass
class PropType35(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE35` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE35"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE36 ------------------------------------------------------
@dataclass
class PropType36(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE36` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE36"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE43 ------------------------------------------------------
@dataclass
class PropType43(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE43` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE43"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE44 ------------------------------------------------------
@dataclass
class PropType44(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE44` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE44"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE45 ------------------------------------------------------
@dataclass
class PropType45(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE45` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE45"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE46 ------------------------------------------------------
@dataclass
class PropType46(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE46` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE46"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE51 ------------------------------------------------------
@dataclass
class PropType51(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE51` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE51"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /QUAD ------------------------------------------------------
@dataclass
class Quad(Keyword):
    """Defines a quadrilateral solid element with 4 nodes
    The element type and formulation are defined on the /PROP card.
    """

    part_id: int
    quad_ids: List[int] | NDArray
    node_ids: List[Tuple[int, ...]] | NDArray

    @property
    def keyword(self):
        return f"/QUAD/{self.part_id}"

    @property
    def pre_conditions(self):
        # FIXME: Preconditions make no sense (taken from impl. of Bric20)
        return [
            (
                len(self.quad_ids) == len(self.node_ids),
                "Pre-condition `len(brick_ids) == len(node_ids)` is violated.",
            ),
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            ArrayOfAtomicFields(
                [
                    IntField("quad_ids", 1),
                    IntField("node_ids:ID_1|0", 2),
                    IntField("node_ids:ID_2|1", 3),
                    IntField("node_ids:ID_3|2", 4),
                    IntField("node_ids:ID_4|3", 5),
                ]
            )
        ]

        return structure


# --- /RADIATION ------------------------------------------------------
@dataclass
class Radiation(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/RADIATION` is not implemented.")

    @property
    def keyword(self):
        return "/RADIATION"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
