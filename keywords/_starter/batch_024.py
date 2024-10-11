#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField, KeywordStructureType

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
        raise NotImplementedError("Keyword `/INTER/TYPE6` is not implemented.")

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
        raise NotImplementedError("Keyword `/INTER/TYPE7` is not implemented.")

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
        raise NotImplementedError("Keyword `/INTER/TYPE8` is not implemented.")

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
        raise NotImplementedError("Keyword `/INTER/TYPE9` is not implemented.")

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
        raise NotImplementedError("Keyword `/INTER/TYPE10` is not implemented.")

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
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#line_ids|-line_idm|----i_stf|----i_the|----i_gap|----6----|i_rem_gap|----i_del|----9----|----10---|"
    )
    line2: str = (
        "#------------st_min|-------------st_max|---------%mesh_size|-------------dt_min|---i_form|--sens_id|"
    )
    line3: str = (
        "#------------st_fac|---------------fric|------------gap_min|------------t_start|-------------t_stop|"
    )
    line4: str = (
        "#----i_bc|----2----|----3----|---inacti|--------------vis_s|--------------vis_f|-------------bumult|"
    )
    line5: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|--fric_id|"
    )
    line6: str = (
        "#-------------k_the|-fct_id_k|----------a_scale_k|--------------t_int|i_theform|----9----|----10---|"
    )
    line7: str = (
        "#-------------f_rad|--------------d_rad|----5----|----6----|----7----|----8----|----9----|----10---|"
    )

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
        structure.append(
            StringField("inter_title", 1, 10),
            StringField("line1", 1, 10),
            IntField("line_id_s", 1),
            IntField("line_id_m", 2),
            IntField("i_stf", 3),
            IntField("i_the", 4),
            IntField("i_gap", 5),
            IntField("irem_gap", 7),
            IntField("i_del", 8),
            StringField("line2", 1, 10),
            FloatField("St_min", 1),
            FloatField("St_max", 3),
            FloatField("mesh_size", 5),
            FloatField("dt_min", 7),
            IntField("i_form", 9),
            IntField("sens_id", 10),
            StringField("line3", 1, 10),
            FloatField("Stfac", 1),
            FloatField("fric", 3),
            FloatField("gap_min", 5),
            FloatField("t_start", 7),
            FloatField("t_stop", 9),
            StringField("line4", 1, 10),
            IntField("i_bc", 1),
            IntField("inacti", 4),
            FloatField("vis_s", 5),
            FloatField("vis_f", 7),
            FloatField("bumult", 9),
            StringField("line5", 1, 10),
            IntField("fric_id", 10),
        )
        if self.i_the > 0:
            structure.append(
                StringField("line6", 1, 10),
                FloatField("k_the", 1),
                IntField("fct_id_k", 3),
                FloatField("a_scale_k", 4),
                FloatField("t_int", 6),
                IntField("i_the_form", 8),
                StringField("line7", 1, 10),
                FloatField("f_rad", 1),
                FloatField("d_rad", 3),
            )
        return structure


# --- /INTER/TYPE12 ------------------------------------------------------
@dataclass
class InterType12(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/INTER/TYPE12` is not implemented.")

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
        raise NotImplementedError("Keyword `/INTER/TYPE14` is not implemented.")

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
