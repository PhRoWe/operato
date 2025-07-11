#!/usr/bin/env python3

from dataclasses import dataclass

from numpy.typing import NDArray

from operato.keywords.common import (
    ArrayOfAtomicFields,
    FloatField,
    IntField,
    StringField,
    Keyword,
    KeywordPreconditionsType,
    KeywordStructureType,
    MultiLineArrayOfAtomicFields,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MONVOL/GAS                 /MONVOL/LFLUID              /MONVOL/PRES
# /MOVE_FUNCT                 /MPC                        /NBCS
# /NODE                       /NONLOCAL/MAT               /PARAMETER
#


# --- /MONVOL/GAS ------------------------------------------------------
@dataclass
class MonvolGas(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MONVOL/GAS` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/GAS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        return structure


# --- /MONVOL/LFLUID ------------------------------------------------------
@dataclass
class MonvolLfluid(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MONVOL/LFLUID` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/LFLUID"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        return structure


# --- /MONVOL/PRES ------------------------------------------------------
@dataclass
class MonvolPres(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MONVOL/PRES` is not implemented.")

    @property
    def keyword(self):
        return "/MONVOL/PRES"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        return structure


# --- /MOVE_FUNCT ------------------------------------------------------
@dataclass
class MoveFunct(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MOVE_FUNCT` is not implemented.")

    @property
    def keyword(self):
        return "/MOVE_FUNCT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        return structure


# --- /MPC ------------------------------------------------------
@dataclass
class Mpc(Keyword):
    id: int

    node_id: list[int]
    idof: list[int]
    skew_id: list[int]
    alpha: list[int]
    title: str = ""
    line0: str = (
        "#-node_id|-----idof|--skew_id|----alpha|----5----|----6----|----7----|----8----|----9----|----10---|"
    )

    @property
    def keyword(self):
        return f"/MPC/{self.id}"

    @property
    def pre_conditions(self):
        # check that all are either ints of of same length
        inputs = [self.node_id, self.idof, self.skew_id, self.alpha]
        conditions = [
            (
                bool(all(len(inputs[0]) == len(x) for x in inputs[1:])),
                "Inconsistent input lengths!",
            ),
        ]
        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("line0", 1, 10),
            StringField("title", 1, 10),
            ArrayOfAtomicFields(
                [
                    IntField("node_id", 1),
                    IntField("idof", 2),
                    IntField("skew_id", 3),
                    IntField("alpha", 4),
                ]
            ),
        ]

        return structure


# --- /NBCS ------------------------------------------------------
@dataclass
class Nbcs(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/NBCS` is not implemented.")

    @property
    def keyword(self):
        return "/NBCS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        return structure


# --- NODE ------------------------------------------------------------------------------------
@dataclass
class Node(Keyword):
    node_ids: list | tuple | NDArray
    xc_yc_zc: NDArray
    unit_id: int | None = None
    add_header: bool = False

    def __post_init__(self) -> None:
        super().__post_init__()

    @property
    def keyword(self):
        if self.unit_id:
            return f"/NODE/{self.unit_id}"
        else:
            return "/NODE"

    @property
    def pre_conditions(self) -> KeywordPreconditionsType:
        return []

    @property
    def structure(self):
        if not hasattr(self.xc_yc_zc, "xc"):
            structure: KeywordStructureType = [
                ArrayOfAtomicFields(
                    (
                        IntField("node_ids", 1),
                        FloatField("xc_yc_zc:yc|0", 2),
                        FloatField("xc_yc_zc:zc|1", 4),
                    )
                )
            ]
        else:
            structure: KeywordStructureType = [
                ArrayOfAtomicFields(
                    (
                        IntField("node_ids", 1),
                        FloatField("xc_yc_zc:xc|0", 2),
                        FloatField("xc_yc_zc:yc|1", 4),
                        FloatField("xc_yc_zc:zc|2", 6),
                    )
                )
            ]

        return structure


# --- /NONLOCAL/MAT ------------------------------------------------------
@dataclass
class NonlocalMat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/NONLOCAL/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/NONLOCAL/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        return structure


# --- /PARAMETER ------------------------------------------------------
@dataclass
class Parameter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/PARAMETER` is not implemented.")

    @property
    def keyword(self):
        return "/PARAMETER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure: KeywordStructureType = []

        return structure
