#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PROP/TYPE8                 /PROP/TYPE9                 /PROP/TYPE10
# /PROP/TYPE11                /PROP/TYPE12                /PROP/TYPE13
# /PROP/TYPE14                /PROP/TYPE14                /PROP/TYPE15
#


# --- /PROP/TYPE8 ------------------------------------------------------
@dataclass
class PropType8(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE8` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE8"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE9 ------------------------------------------------------
@dataclass
class PropType9(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE9` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE9"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE10 ------------------------------------------------------
@dataclass
class PropType10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE10` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE11 ------------------------------------------------------
@dataclass
class PropType11(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE11` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE11"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE12 ------------------------------------------------------
@dataclass
class PropType12(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE12` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE12"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE13 ------------------------------------------------------
@dataclass
class PropType13(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE13` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE13"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE14 ------------------------------------------------------
@dataclass
class PropType14(Keyword):
    prop_id: int
    unit_id: int | None = None
    prop_title: str = ""
    i_solid: int | None = None
    i_smstr: int | None = None
    i_ale: int | None = None
    i_cpre: int | None = None
    i_tetra10: int | None = None
    i_npts: int | None = None
    i_tetra4: int | None = None
    i_frame: int | None = None
    d_n: float | None = None
    q_a: float | None = None
    q_b: float | None = None
    h: float | None = None
    lambda_v: float | None = None
    mu_v: float | None = None
    dt_min: float | None = None
    Vdef_min: float | None = None
    Vdef_max: float | None = None
    aps_max: float | None = None
    col_min: float | None = None
    Ndir: int | None = None
    sphpart_id: int | None = None
    # commentary lines for better readability:
    line1: str = (
        "#   Isolid    Ismstr               Icpre  Itetra10     Inpts   Itetra4    Iframe                  dn"
    )
    line2: str = (
        "#                q_a                 q_b                   h            LAMBDA_V                MU_V"
    )
    line3: str = (
        "#             dt_min            Vdef_min            Vdef_max             APS_max             COL_min"
    )
    line4: str = "#              N_dir          sphpart_id"
    add_separator: bool = True

    @property
    def keyword(self):
        if self.unit_id is not None:
            return f"/PROP/TYPE14/{self.prop_id}/{self.unit_id}"
        else:
            return f"/PROP/TYPE14/{self.prop_id}"

    @property
    def pre_conditions(self):
        if self.i_cpre == -1:
            # use -1 as "no user input" flag and find correct rules for choosing based on i_solid
            if self.i_solid == 17:
                self.i_cpre = 1
            elif self.i_solid == 14 or self.i_solid == 24:
                self.i_cpre = 3
        return []

    @property
    def structure(self):
        structure = [
            StringField("prop_title", 1, 3),
            StringField("line1", 1, 10),
            [
                IntField("i_solid", 1),
                IntField(
                    "i_smstr",
                    2,
                ),
                IntField("i_ale", 3),
                IntField("i_cpre", 4),
                IntField("i_tetra10", 5),
                IntField("i_npts", 6),
                IntField("i_tetra4", 7),
                IntField("i_frame", 8),
                FloatField("d_n", 9),
            ],
            StringField("line2", 1, 10),
            [
                FloatField("q_a", 1),
                FloatField("q_b", 3),
                FloatField("h", 5),
                FloatField("lambda_v", 7),
                FloatField("mu_v", 9),
            ],
            StringField("line3", 1, 10),
            [
                FloatField("dt_min", 1),
                FloatField("Vdef_min", 3),
                FloatField("Vdef_max", 5),
                FloatField("aps_max", 7),
                FloatField("col_min", 9),
            ],
        ]
        if self.Ndir is not None and self.sphpart_id is not None:
            structure.append(
                [
                    IntField("Ndir", 1),
                    IntField(
                        "sphpart_id",
                        2,
                    ),
                ]
            )
        return structure


# --- /PROP/TYPE15 ------------------------------------------------------
@dataclass
class PropType15(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE15` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE15"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
