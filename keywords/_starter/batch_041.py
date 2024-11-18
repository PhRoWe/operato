#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PROP/INJECT1               /PROP/INJECT2               /PROP/PCOMPP
# /PROP/TYPE0                 /PROP/TYPE1                 /PROP/TYPE2
# /PROP/TYPE3                 /PROP/TYPE4                 /PROP/TYPE6
#


# --- /PROP/INJECT1 ------------------------------------------------------
@dataclass
class PropInject1(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/INJECT1` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/INJECT1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/INJECT2 ------------------------------------------------------
@dataclass
class PropInject2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/INJECT2` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/INJECT2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/PCOMPP ------------------------------------------------------
@dataclass
class PropPcompp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/PCOMPP` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/PCOMPP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE0 ------------------------------------------------------
@dataclass
class PropType0(Keyword):
    prop_id: int
    prop_title: str | None = None
    unit_id: int | None = None
    line00: str = "#/PROP/TYPE0/prop_ID/unit_ID\n"

    @property
    def keyword(self):
        if self.unit_id is not None:
            return self.line00 + f"/PROP/TYPE0/{self.prop_id}/{self.unit_id}"
        else:
            return self.line00 + f"/PROP/TYPE0/{self.prop_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [StringField("prop_title", 1, 10)]

        return structure


# --- /PROP/TYPE1 ------------------------------------------------------
@dataclass
class PropType1(Keyword):
    """Defines Radioss PropType1 (SHELL) Doc:(https://help.altair.com/hwsolvers/rad/topics/solvers/rad/prop_type1_shell_starter_r.htm)"""

    prop_id: int
    t: float
    unit_id: int | None = None
    prop_title: str = ""
    i_shell: int | None = None
    i_smstr: int | None = None
    i_sh3n: int | None = None
    i_drill: int | None = None
    i_thick: int | None = None
    i_plas: int | None = None
    p_thick_fail: float | None = None
    h_m: float | None = None
    h_f: float | None = None
    h_r: float | None = None
    d_m: float | None = None
    d_n: float | None = None
    n: int | None = None
    a_shear: float | None = None
    # commentary lines for better readability:
    line00: str = "#/PROP/TYPE1/prop_ID/unit_ID\n"
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#--Ishell|---Ismstr|----Ish3n|---Idrill|----5----|----6----|------P_thick_fail-|----9----|----10---|"
    )
    line2: str = (
        "#----------------hm|-----------------hf|-----------------hr|-----------------dm|-----------------dn|"
    )
    line3: str = (
        "#-------N|--Istrain|--------------Thick|-------------Ashear|----7----|---Ithick|----Iplas|----10---|"
    )
    add_separator: bool = True

    @property
    def keyword(self):
        if self.unit_id is not None:
            return self.line00 + f"/PROP/TYPE1/{self.prop_id}/{self.unit_id}"
        else:
            return self.line00 + f"/PROP/TYPE1/{self.prop_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            StringField("prop_title", 1, 3),
            StringField("line1", 1, 10),
            [
                IntField("i_shell", 1),
                IntField("i_smstr", 2),
                IntField("i_sh3n", 3),
                IntField("i_drill", 4),
                FloatField("p_thick_fail", 7),
            ],
            StringField("line2", 1, 10),
            [
                FloatField("h_m", 1),
                FloatField("h_f", 3),
                FloatField("h_r", 5),
                FloatField("d_m", 7),
                FloatField("d_n", 9),
            ],
            StringField("line3", 1, 10),
            [
                IntField("n", 1),
                FloatField("t", 3),
                FloatField("a_shear", 5),
                IntField("i_thick", 8),
                IntField("i_plas", 9),
            ],
        ]

        return structure


# --- /PROP/TYPE2 ------------------------------------------------------
@dataclass
class PropType2(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE2` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE2"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE3 ------------------------------------------------------
@dataclass
class PropType3(Keyword):
    """Describes the beam property for torsion, bending, membrane or axial deformation.
    https://help.altair.com/hwsolvers/rad/topics/solvers/rad/prop_type3_beam_starter_r.htm#prop_type3_beam_starter_r__section_nvk_khm_n1c
    """

    prop_id: int
    area: float
    i_yy: float
    i_zz: float
    i_xx: float
    I_shear: int
    unit_id: int | None = None
    prop_title: str | None = None
    I_smstr: int = 0
    d_m: float | None = None
    d_f: float | None = None

    omega_dof: str | None = "   000 000"
    # lines added for readability of input deck
    line00: str = "#/PROP/TYPE3/prop_ID/unit_ID\n"
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#---1----|--i_smstr|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line2: str = (
        "#---------------d_m|----------------d_f|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line3: str = (
        "#--------------area|---------------I_yy|---------------I_zz|---------------I_xx|----9----|----10---|"
    )
    line4: str = (
        "#omegadof|--i_shear|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )

    @property
    def keyword(self):
        if self.unit_id is not None:
            return self.line00 + f"/PROP/TYPE3/{self.prop_id}/{self.unit_id}"
        else:
            return self.line00 + f"/PROP/TYPE3/{self.prop_id}"

    @property
    def pre_conditions(self):
        cond = []

        return cond

    @property
    def structure(self):
        # Basic structure
        structure = [
            StringField("line0", 1, 10),
            StringField("prop_title", 1, 3),
            StringField("line1", 1, 10),
            [
                IntField("I_smstr", 2),
            ],
            StringField("line2", 1, 10),
            [
                FloatField("d_m", 1),
                FloatField("d_f", 3),
            ],
            StringField("line3", 1, 10),
            [
                FloatField("area", 1),
                FloatField("i_yy", 3),
                FloatField("i_zz", 5),
                FloatField("i_xx", 7),
            ],
        ]
        structure.append(StringField("line4", 1, 10))
        structure.append([StringField("omega_dof", 1, 1), IntField("I_shear", 2)])

        return structure


# --- /PROP/TYPE4 ------------------------------------------------------
@dataclass
class PropType4(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PROP/TYPE4` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE4"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PROP/TYPE6 ------------------------------------------------------
@dataclass
class PropType6(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/PROP/TYPE6` is not implemented.")

    @property
    def keyword(self):
        return "/PROP/TYPE6"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
