#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField, KeywordStructureType

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PART                       /PENTA6                     /PERTURB
# /PERTURB/FAIL/BIQUAD        /PERTURB/PART/SHELL         /PERTURB/PART/SOLID
# /PLOAD                      /PLY                        /PRELOAD
#


# --- /PART ------------------------------------------------------
@dataclass
class Part(Keyword):
    part_id: int
    part_title: str
    prop_id: int
    mat_id: int
    unit_id: int | None = None
    subset_id: int = None
    Thick: float = None

    @property
    def keyword(self):
        if self.unit_id is not None:
            return f"/PART/{self.part_id}/{self.unit_id}"
        else:
            return f"/PART/{self.part_id}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [StringField("part_title", 1, 3)]
        structure2 = [IntField("prop_id", 1), IntField("mat_id", 2)]
        if self.subset_id is not None:
            structure2.append(IntField("subset_id", 3))
        if self.Thick is not None:
            structure2.append(FloatField("Thick", 5))
        structure = [structure, structure2]

        return structure


# --- /PENTA6 ------------------------------------------------------
@dataclass
class Penta6(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PENTA6` is not implemented.")

    @property
    def keyword(self):
        return "/PENTA6"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PERTURB ------------------------------------------------------
@dataclass
class Perturb(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PERTURB` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PERTURB/FAIL/BIQUAD ------------------------------------------------------
@dataclass
class PerturbFailBiquad(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PERTURB/FAIL/BIQUAD` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB/FAIL/BIQUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PERTURB/PART/SHELL ------------------------------------------------------
@dataclass
class PerturbPartShell(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PERTURB/PART/SHELL` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB/PART/SHELL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PERTURB/PART/SOLID ------------------------------------------------------
@dataclass
class PerturbPartSolid(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PERTURB/PART/SOLID` is not implemented.")

    @property
    def keyword(self):
        return "/PERTURB/PART/SOLID"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PLOAD ------------------------------------------------------
@dataclass
class Pload(Keyword):
    """Defines pressure load on a surface.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/pload_starter_r.htm)
    """

    pload_id: int
    unit_id: int
    surf_id: int
    fct_id_t: int
    sens_id: int
    pload_title: str | None = None
    I_del: int | None = None
    a_scale_x: float | None = 1.0
    f_scale_y: float | None = 1.0
    # added line for readability
    line00: str = "#/PLOAD/pload_ID/unit_ID\n"
    line0: str = (
        "#---1----|----2----|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line1: str = (
        "#-surf_ID|-fct_ID_T|--sens_ID|----4----|----I_del|----6----|-----------Ascale_x|-----------Fscale_y|"
    )

    @property
    def keyword(self):
        return self.line00 + f"/PLOAD/{self.pload_id}/{self.unit_id}"

    @property
    def pre_conditions(self):
        conditions = []
        if self.I_del is not None:
            conditions = [
                [(self.I_del == 1 or self.I_del == 2, "Unknown setting for I_del!")]
            ]
        return conditions

    @property
    def structure(self):
        structure: KeywordStructureType = [
            StringField("pload_title", 1, 10),
            StringField("line1", 1, 10),
            [
                IntField("surf_id", 1),
                IntField("fct_id_t", 2),
                IntField("sens_id", 3),
                IntField("I_del", 5),
                FloatField("a_scale_x", 7),
                FloatField("f_scale_y", 9),
            ],
        ]
        return structure


# --- /PLY ------------------------------------------------------
@dataclass
class Ply(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/PLY` is not implemented.")

    @property
    def keyword(self):
        return "/PLY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PRELOAD ------------------------------------------------------
@dataclass
class Preload(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/PRELOAD` is not implemented.")

    @property
    def keyword(self):
        return "/PRELOAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
