#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField
from operato.constants import UNKNOWN_INPUT

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /BCSR/ROT                   /BCSR/TRA                   /DAMP
# /DEL                        /DEL/Eltyp/1                /DEL/INTER
# /DELINT                     /DT                         /DT/AIRBAG/Keyword3
#


# --- /BCSR/ROT ------------------------------------------------------
@dataclass
class BcsrRot(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/BCSR/ROT` is not implemented.")

    @property
    def keyword(self):
        return "/BCSR/ROT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /BCSR/TRA ------------------------------------------------------
@dataclass
class BcsrTra(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/BCSR/TRA` is not implemented.")

    @property
    def keyword(self):
        return "/BCSR/TRA"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DAMP ------------------------------------------------------
@dataclass
class Damp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DAMP` is not implemented.")

    @property
    def keyword(self):
        return "/DAMP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DEL ------------------------------------------------------
@dataclass
class Del(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DEL` is not implemented.")

    @property
    def keyword(self):
        return "/DEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DEL/Eltyp/1 ------------------------------------------------------
@dataclass
class DelEltyp1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DEL/Eltyp/1` is not implemented.")

    @property
    def keyword(self):
        return "/DEL/Eltyp/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DEL/INTER ------------------------------------------------------
@dataclass
class DelInter(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DEL/INTER` is not implemented.")

    @property
    def keyword(self):
        return "/DEL/INTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DELINT ------------------------------------------------------
@dataclass
class Delint(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DELINT` is not implemented.")

    @property
    def keyword(self):
        return "/DELINT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT ------------------------------------------------------
@dataclass
class Dt(Keyword):
    dTmin: float
    dT_sca: float
    # added commentary line for readability of input deck
    line0: str = "#/DT\n"
    add_header: bool = True

    @property
    def keyword(self):
        return self.line0 + f"/DT"

    @property
    def pre_conditions(self):
        conditions = []
        conditions.append(
            [
                (self.dT_sca is not None, UNKNOWN_INPUT + "dT_sca"),
                (self.dTmin is not None, UNKNOWN_INPUT + "dTmin"),
            ]
        )
        return []

    @property
    def structure(self):
        structure = []
        structure.append(
            [FloatField("dT_sca", 1), FloatField("dTmin", 3)],
        )
        return structure


# --- /DT/AIRBAG/Keyword3 ------------------------------------------------------
@dataclass
class DtAirbagKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/DT/AIRBAG/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/DT/AIRBAG/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
