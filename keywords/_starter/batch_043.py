#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

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
        raise NotImplementedError("Keyword `/PROP/TYPE16` is not implemented.")

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
        raise NotImplementedError("Keyword `/PROP/TYPE17` is not implemented.")

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
    unit_id: int | None = None
    prop_title: str | None = None
    i_sect: int | None = None
    i_smstr: int | None = None
    d_m: float | None = None
    d_f: float | None = None
    NIP: int | None = None
    i_ref: int | None = None
    y_0: float | None = None
    z_0: float | None = None
    # lines added for readability of input deck
    line1: str = "#   i_sec      i_smstr"
    line2: str = "#                  d_m                  d_f"
    line3: str = "#     NIP        i_ref                  y_0                  z_0"

    @property
    def keyword(self):
        if self.unit_id is not None:
            return f"/PROP/TYPE18/{self.prop_id}/{self.unit_id}"
        else:
            return f"/PROP/TYPE18/{self.prop_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("prop_title", 1, 3),
            StringField("line1", 1, 10),
            [
                IntField("i_sect", 1),
                IntField("i_smstr", 2),
            ],
            StringField("line2", 1, 10),
            [
                FloatField("d_m", 1),
                FloatField("d_f", 3),
            ],
            StringField("line3", 1, 10),
            [
                IntField("NIP", 1),
                IntField("i_ref", 2),
                FloatField("y_0", 3),
                FloatField("z_0", 5),
            ],
        ]

        return structure


# --- /PROP/TYPE19 ------------------------------------------------------
@dataclass
class PropType19(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PROP/TYPE19` is not implemented.")

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
        raise NotImplementedError("Keyword `/PROP/TYPE20` is not implemented.")

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
        raise NotImplementedError("Keyword `/PROP/TYPE21` is not implemented.")

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
        raise NotImplementedError("Keyword `/PROP/TYPE22` is not implemented.")

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
        raise NotImplementedError("Keyword `/PROP/TYPE23` is not implemented.")

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
