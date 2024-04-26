#!/usr/bin/env python3

from dataclasses import dataclass

from ..common import FloatField, IntField, Keyword, StringField

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
            structure2.append(IntField(subset_id, 3))
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
        raise NotImplementedError("Keyword `/PENTA6` is not implemented.")

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
        raise NotImplementedError("Keyword `/PERTURB` is not implemented.")

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
        raise NotImplementedError("Keyword `/PERTURB/FAIL/BIQUAD` is not implemented.")

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
        raise NotImplementedError("Keyword `/PERTURB/PART/SHELL` is not implemented.")

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
        raise NotImplementedError("Keyword `/PERTURB/PART/SOLID` is not implemented.")

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
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PLOAD` is not implemented.")

    @property
    def keyword(self):
        return "/PLOAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /PLY ------------------------------------------------------
@dataclass
class Ply(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        raise NotImplementedError("Keyword `/PLY` is not implemented.")

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
