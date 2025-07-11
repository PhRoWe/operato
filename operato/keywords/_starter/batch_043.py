#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    ArrayOfAtomicFields,
)
from typing import List

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PROP/TYPE16                /PROP/TYPE17                /PROP/TYPE18
# /PROP/TYPE19                /PROP/TYPE20                /PROP/TYPE21
# /PROP/TYPE22                /PROP/TYPE23                /PROP/TYPE25
#


# --- /PROP/TYPE16 ------------------------------------------------------
@dataclass
class PropType16(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE16` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE16"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE17 ------------------------------------------------------
@dataclass
class PropType17(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE17` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE17"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE18 ------------------------------------------------------
@dataclass
class PropType18(Keyword):
    prop_id: int
    i_sect: int
    unit_id: int | None = None
    prop_title: str | None = None
    i_smstr: int | None = None
    d_m: float | None = None
    d_f: float | None = None
    NIP: int | None = None
    i_ref: int | None = None
    y_0: float | None = None
    z_0: float | None = None
    y_i: List[float] | None = None
    z_i: List[float] | None = None
    area: float | None = None  # only for i_sect=0
    nitr: int | None = None
    l1: float | None = None
    l2: float | None = None
    omega_dof: str | None = "   000 000"
    # lines added for readability of input deck
    line00: str = "#/PROP/TYPE18/prop_ID/unit_ID\n"
    add_header: bool = True

    @property
    def keyword(self):
        if self.unit_id is not None:
            return self.line00 + f"/PROP/TYPE18/{self.prop_id}/{self.unit_id}"
        else:
            return self.line00 + f"/PROP/TYPE18/{self.prop_id}"

    @property
    def pre_conditions(self):
        if self.i_sect == 0 and self.i_ref is None:
            self.i_ref = 0
        if self.i_sect > 0:
            if self.i_sect == 1 or self.i_sect == 3:
                if self.l2 is None:
                    self.l2 = self.l1
        cond = [
            (
                (self.i_sect == 0 and self.NIP is not None)
                or (self.i_sect != 0 and self.NIP is None),
                "NIP only to be defined if i_sect==0.",
            ),
            (
                (self.i_sect == 0 and self.i_ref is not None)
                or (self.i_sect != 0 and self.i_ref is None),
                "I_ref only to be defined if i_sect==0.",
            ),
            (
                (self.i_ref != 1 and self.y_0 is None and self.z_0 is None)
                or (self.i_ref == 1 and self.y_0 is not None and self.z_0 is not None),
                "Define subsection center if I_ref==1.",
            ),
            (
                (self.z_i is not None and self.i_sect == 0 and self.NIP is not None)
                or (self.z_i is None and self.i_sect != 0 and self.NIP is None),
                "Z_i needs to be defined if i_sect==0 and NIP>0.",
            ),
            (
                (self.area is not None and self.i_sect == 0 and self.NIP is not None)
                or (self.area is None and self.i_sect != 0 and self.NIP is None),
                "area needs to be defined if i_sect==0.",
            ),
            (
                (self.nitr is None and self.i_sect == 0)
                or (self.nitr is not None and self.i_sect != 0),
                "Define the integration points since i_sect>0.",
            ),
            (
                (self.l1 is None and self.i_sect == 0)
                or (self.l1 is not None and self.i_sect != 0),
                "Define the first size of the predefined section since i_sect>0.",
            ),
        ]

        return cond

    @property
    def structure(self):
        # Basic structure
        structure = [
            StringField("line0", 1, 10),
            StringField("prop_title", 1, 3),
            [
                IntField("i_sect", 1),
                IntField("i_smstr", 2),
            ],
            [
                FloatField("d_m", 1),
                FloatField("d_f", 3),
            ],
            [
                IntField("NIP", 1),
                IntField("i_ref", 2),
                FloatField("y_0", 3),
                FloatField("z_0", 5),
            ],
        ]
        if self.NIP is not None:
            structure.append(
                ArrayOfAtomicFields(
                    [
                        FloatField("y_i", 1),
                        FloatField("z_i", 3),
                        FloatField("area", 5),
                    ]
                )
            )
        if self.nitr is not None:
            structure.append(
                [IntField("nitr", 1), FloatField("l1", 3), FloatField("l2", 5)]
            )
        structure.append(StringField("omega_dof", 1, 10))

        return structure


# --- /PROP/TYPE19 ------------------------------------------------------
@dataclass
class PropType19(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE19` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE19"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE20 ------------------------------------------------------
@dataclass
class PropType20(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE20` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE20"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE21 ------------------------------------------------------
@dataclass
class PropType21(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE21` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE21"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE22 ------------------------------------------------------
@dataclass
class PropType22(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE22` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE22"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE23 ------------------------------------------------------
@dataclass
class PropType23(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE23` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE23"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE25 ------------------------------------------------------
@dataclass
class PropType25(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/PROP/TYPE25` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE25"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
