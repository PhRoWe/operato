#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List, Literal, Sequence, Tuple, get_args

from numpy.typing import NDArray
from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    KeywordStructureType,
    ArrayOfAtomicFields,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /SENSOR/SENS                /SENSOR/TIME                /SENSOR/VEL
# /SENSOR/WORK                /SET                        /SH3N
# /SHELL                      /SHEL16                     /SKEW/FIX
#


# --- /SENSOR/SENS ------------------------------------------------------
@dataclass
class SensorSens(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/SENSOR/SENS` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/SENS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SENSOR/TIME ------------------------------------------------------
@dataclass
class SensorTime(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/SENSOR/TIME` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/TIME"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SENSOR/VEL ------------------------------------------------------
@dataclass
class SensorVel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/SENSOR/VEL` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/VEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SENSOR/WORK ------------------------------------------------------
@dataclass
class SensorWork(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/SENSOR/WORK` is not implemented.")

    @property
    def keyword(self):
        return "/SENSOR/WORK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SET ------------------------------------------------------
@dataclass
class Set(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/SET` is not implemented.")

    @property
    def keyword(self):
        return "/SET"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SH3N ------------------------------------------------------
@dataclass
class Sh3n(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/SH3N` is not implemented.")

    @property
    def keyword(self):
        return "/SH3N"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SHELL ------------------------------------------------------
@dataclass
class Shell(Keyword):
    """Defines a quadrilateral shell with 4 nodes. Doc: (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/shell_starter_r.htm)
    The element type and formulation are defined on the /PROP card.
    """

    part_id: int
    shell_ids: List[int] | NDArray
    node_ids: List[Tuple[int, ...]] | NDArray
    t: List[Tuple[int, ...]] | NDArray
    phi: List[Tuple[int, ...]] | NDArray
    unit_id: int | None = None

    @property
    def keyword(self):
        if self.unit_id is not None:
            return f"/SHELL/{self.part_id}/{self.unit_id}"
        else:
            return f"/SHELL/{self.part_id}"

    @property
    def pre_conditions(self):
        return [
            (
                len(self.shell_ids) == len(self.node_ids),
                "Pre-condition `len(brick_ids) == len(node_ids)` is violated.",
            ),
        ]

    @property
    def structure(self):
        structure: KeywordStructureType = [
            ArrayOfAtomicFields(
                [
                    IntField("shell_ids", 1),
                    IntField("node_ids:ID_1|0", 2),
                    IntField("node_ids:ID_2|1", 3),
                    IntField("node_ids:ID_3|2", 4),
                    IntField("node_ids:ID_4|3", 5),
                    FloatField("phi", 6),
                    FloatField("t", 9),
                ]
            )
        ]

        return structure


# --- /SHEL16 ------------------------------------------------------
@dataclass
class Shel16(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/SHEL16` is not implemented.")

    @property
    def keyword(self):
        return "/SHEL16"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /SKEW/FIX ------------------------------------------------------
@dataclass
class SkewFix(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SKEW/FIX` is not implemented.")

    @property
    def keyword(self):
        return "/SKEW/FIX"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
