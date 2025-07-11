#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    KeywordStructureType,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /INTER/TYPE6                /INTER/TYPE7                /INTER/TYPE8
# /INTER/TYPE9                /INTER/TYPE10               /INTER/TYPE11
# /INTER/TYPE12               /INTER/TYPE14               /INTER/TYPE15
#


# --- /INTER/TYPE6 ------------------------------------------------------
@dataclass
class InterType6(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INTER/TYPE6` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE6"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INTER/TYPE7 ------------------------------------------------------
@dataclass
class InterType7(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INTER/TYPE7` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE7"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INTER/TYPE8 ------------------------------------------------------
@dataclass
class InterType8(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INTER/TYPE8` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE8"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INTER/TYPE9 ------------------------------------------------------
@dataclass
class InterType9(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INTER/TYPE9` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE9"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INTER/TYPE10 ------------------------------------------------------
@dataclass
class InterType10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INTER/TYPE10` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INTER/TYPE11 ------------------------------------------------------
@dataclass
class InterType11(Keyword):
    """This interface simulates impact between edge to Edge or lines. A line can be a
    beam or truss element or a shell edge or spring elements.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/inter_type11_starter_r.htm)
    #FIXME: Faulty implementation!
    """

    inter_id: int
    lambdaine_id_s: int
    line_id_m: int
    dtmin: float
    fric: float
    gap_min: float
    t_start: float
    t_stop: float
    i_bc: bool
    t_int: float
    f_rad: float
    d_rad: float
    line_id_s: int
    unit_id: int | None = None
    inter_title: str | None = ""
    i_stf: int | None = None
    i_the: int | None = None
    i_gap: int | None = None
    irem_gap: int | None = None
    St_min: float | None = None
    St_max: float | None = None
    mesh_size: float | None = None
    i_form: int | None = None
    sens_id: int | None = None
    i_del: int | None = None
    Stfac: float | None = None
    inacti: int | None = None
    vis_s: float | None = None
    vis_f: float | None = None
    bumult: float | None = None
    fric_id: int | None = None
    k_the: float | None = None
    fct_id_k: int | None = None
    a_scale_k: float | None = None
    i_the_form: int | None = None
    line00: str = "/INTER/TYPE11/inter_ID/unit_ID"
    add_header: bool = False

    @property
    def keyword(self):
        if self.unit_id is not None:
            return self.line00 + f"/INTER/TYPE11/{self.inter_id}/{self.unit_id}"
        else:
            return self.line00 + f"/INTER/TYPE11/{self.inter_id}"

    @property
    def pre_conditions(self):
        conditions = []
        if self.i_stf != 1:
            conditions.append((self.St_min is not None, "St_min needs to be defined "))
            conditions.append((self.St_max is not None, "St_max needs to be defined "))
        if self.i_stf == 1:
            conditions.append(
                (self.St_min is None, "St_min not to be defines if i_stf==1 ")
            )
            conditions.append(
                (self.St_max is None, "St_max not to be defines if i_stf==1 ")
            )
        if self.i_gap == 3:
            conditions.append(
                (self.mesh_size is not None, "Define %mesh_size if i_gap==3")
            )
        if self.i_gap != 3:
            conditions.append(
                (self.mesh_size is None, "Define %mesh_size only if i_gap==3")
            )
        return []

    @property
    def structure(self):
        structure: KeywordStructureType
        structure = [StringField("inter_title", 1, 10)]
        for i, attr in enumerate(
            ["line_id_s", "line_id_m", "i_stf", "i_the", "i_gap", "irem_gap", "i_del"]
        ):
            match getattr(self, attr):
                case int():
                    structure.append(IntField(attr, i + 1))
                case float():
                    structure.append(FloatField(attr, i + 1))
                case None:
                    continue
        for i, attr in enumerate(
            ["St_min", "St_max", "mesh_size", "dtmin", "i_form", "sens_id"]
        ):
            match getattr(self, attr):
                case int():
                    structure.append(IntField(attr, i + 1))
                case float():
                    structure.append(FloatField(attr, i + 1))
                case None:
                    continue
        for i, attr in enumerate(["Stfac", "fric", "gap_min", "t_start", "t_stop"]):
            match getattr(self, attr):
                case int():
                    structure.append(IntField(attr, i + 1))
                case float():
                    structure.append(FloatField(attr, i + 1))
                case None:
                    continue
        for i, attr in enumerate(
            ["i_bc", "inacti", "vis_s", "vis_f", "bumult", "fric_id"]
        ):
            match getattr(self, attr):
                case int():
                    structure.append(IntField(attr, i + 1))
                case float():
                    structure.append(FloatField(attr, i + 1))
                case None:
                    continue
        if self.i_the is not None:
            structure.append(
                [
                    FloatField("k_the", 1),
                    IntField("fct_id_k", 3),
                    FloatField("a_scale_k", 4),
                    FloatField("t_int", 6),
                    IntField("i_the_form", 8),
                    FloatField("f_rad", 1),
                    FloatField("d_rad", 3),
                ]
            )
        return structure


# --- /INTER/TYPE12 ------------------------------------------------------
@dataclass
class InterType12(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INTER/TYPE12` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE12"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INTER/TYPE14 ------------------------------------------------------
@dataclass
class InterType14(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INTER/TYPE14` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE14"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INTER/TYPE15 ------------------------------------------------------
@dataclass
class InterType15(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/INTER/TYPE15` is not implemented.")

    @property
    def keyword(self):
        return "/INTER/TYPE15"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
