#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW10                  /MAT/LAW11                  /MAT/LAW12
# /MAT/LAW14                  /MAT/LAW15                  /MAT/LAW16
# /MAT/LAW18                  /MAT/LAW19                  /MAT/LAW20
#


# --- /MAT/LAW10 ------------------------------------------------------
@dataclass
class MatLaw10(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW10` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW10"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW11 ------------------------------------------------------
@dataclass
class MatLaw11(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW11` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW11"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW12 ------------------------------------------------------
@dataclass
class MatLaw12(Keyword):
    """This law describes a solid material using the Tsai-Wu formulation that is usually
    used to model composites. This material is assumed to be 3D orthotropic-elastic
    before the Tsai-Wu criterion is reached. The material becomes nonlinear afterwards.
    The Tsai-Wu criterion can be set dependent on the plastic work and strain rate in
    each of the orthotropic directions and in shear to model material hardening.
    Stress based orthotropic criterion for brittle damage and failure is available.
    This material is a generalization and improvement of /MAT/LAW14 (COMPSO).
    https://help.altair.com/hwsolvers/rad/topics/solvers/rad/mat_law12_3d_comp_starter_r.htm
    """

    # NON-DEFAULTS:
    mat_id: int
    rho: float
    E11: float
    E22: float
    E33: float
    nu12: float
    nu13: float
    nu23: float
    G12: float
    G13: float
    G23: float
    depsdt_0: float
    B: float
    # DEFAULTS:
    mat_title: str = ""
    unit_id: int | None = None
    sigt1: float = 10**30
    sigt2: float = sigt1
    sigt3: float = sigt2
    delta: float = 0.05
    n: float = 1.0
    f_max: float = 10**10
    W_p_ref: float = 1.0
    sigt1y: float = 0.0
    sigt2y: float = 0.0
    sigc1y: float = 0.0
    sigc2y: float = 0.0
    sigt3y: float = 0.0
    sigt12y: float = 0.0
    sigc12y: float = 0.0
    sigt23y: float = 0.0
    sigc23y: float = 0.0
    alpha: float = 0.0
    Ef: float = 0.0
    c: float = 0.0
    add_header: bool = True

    @property
    def keyword(self):
        line0 = "#/MAT/LAW12/mat_ID(/unit_id)\n"
        line = f"/MAT/LAW12/{self.mat_id}"
        if self.unit_id is not None:
            line += f"/{self.unit_id}"
        return line0 + line

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []
        structure.append(StringField("mat_title", 1, 10))
        structure.append(FloatField("rho", 1))
        # line2
        substructure = []
        for i, attr in enumerate(["E11", "E22", "E33"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line3
        substructure = []
        for i, attr in enumerate(["nu12", "nu23", "nu13"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line4
        substructure = []
        for i, attr in enumerate(["G12", "G23", "G13"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line5
        substructure = []
        for i, attr in enumerate(["sigt1", "sigt2", "sigt3", "delta"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line6
        substructure = []
        for i, attr in enumerate(["B", "n", "f_max", "W_p_ref"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line7
        substructure = []
        for i, attr in enumerate(["sigt1y", "sigt2y", "sigc1y", "sigc2y"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line8
        substructure = []
        for i, attr in enumerate(["sigt12y", "sigc12y", "sigt23y", "sigc23y"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line9
        substructure = []
        for i, attr in enumerate(["alpha", "Ef", "c", "depsdt_0"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        return structure


# --- /MAT/LAW14 ------------------------------------------------------
@dataclass
class MatLaw14(Keyword):
    """This law describes an orthotropic solid material using the Tsai-Wu formulation
    that is mainly designed to model uni-directional composites. This material is
    assumed to be 3D orthotropic-elastic before the Tsai-Wu criterion is reached.
    The material becomes nonlinear afterwards.The nonlinearity in direction 3 is the
    same as that in direction 2 to represent the behavior of a composite matrix
    material. The Tsai-Wu criterion can be set dependent on the plastic work and strain
    rate in each of the orthotropic directions and in shear to model material hardening.
    Stress based orthotropic criterion for brittle damage and failure is available.
    /MAT/LAW12 (3D_COMP) is an improved version of this material and should be used
    instead of LAW14.

    https://help.altair.com/hwsolvers/rad/topics/solvers/rad/mat_law14_compso_starter_r.htm#mat_law14_compso_starter_r__section_kvg_khm_n1c

    """

    # NON-DEFAULTS:
    mat_id: int
    rho: float
    E11: float
    E22: float
    E33: float
    nu12: float
    nu13: float
    nu23: float
    G12: float
    G13: float
    G23: float
    depsdt_0: float
    B: float
    # DEFAULTS:
    mat_title: str = ""
    unit_id: int | None = None
    sigt1: float = 10**30
    sigt2: float = sigt1
    sigt3: float = sigt2
    delta: float = 0.05
    n: float = 1.0
    f_max: float = 10**10
    W_p_ref: float = 1.0
    sigt1y: float = 0.0
    sigt2y: float = 0.0
    sigc1y: float = 0.0
    sigc2y: float = 0.0
    sigt3y: float = 0.0
    sigt12y: float = 0.0
    sigc12y: float = 0.0
    sigt23y: float = 0.0
    sigc23y: float = 0.0
    alpha: float = 0.0
    Ef: float = 0.0
    c: float = 0.0
    ICC: int = 1
    add_header: bool = True

    @property
    def keyword(self):
        line0 = "#/MAT/LAW14/mat_ID(/unit_id)\n"
        line = f"/MAT/LAW14/{self.mat_id}"
        if self.unit_id is not None:
            line += f"/{self.unit_id}"
        return line0 + line

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [StringField("mat_title", 1, 10), FloatField("rho", 1)]
        structure.append(
            [FloatField("E11", 1), FloatField("E22", 3), FloatField("E33", 5)]
        )
        structure.append(
            [FloatField("nu12", 1), FloatField("nu23", 3), FloatField("nu13", 5)]
        )
        structure.append(
            [FloatField("G12", 1), FloatField("G23", 3), FloatField("G13", 5)]
        )
        structure.append(
            [
                FloatField("sigt1", 1),
                FloatField("sigt2", 3),
                FloatField("sigt3", 5),
                FloatField("delta", 7),
            ]
        )
        structure.append(
            [
                FloatField("B", 1),
                FloatField("n", 3),
                FloatField("f_max", 5),
                FloatField("W_p_ref", 7),
            ]
        )
        structure.append(
            [
                FloatField("sigt1y", 1),
                FloatField("sigt2y", 3),
                FloatField("sigc1y", 5),
                FloatField("sigc2y", 7),
            ]
        )
        structure.append(
            [
                FloatField("sigt12y", 1),
                FloatField("sigc12y", 3),
                FloatField("sigt23y", 5),
                FloatField("sigc23y", 7),
            ]
        )
        structure.append(
            [
                FloatField("alpha", 1),
                FloatField("Ef", 3),
                FloatField("c", 5),
                FloatField("depsdt_0", 7),
                IntField("ICC", 9),
            ]
        )
        return structure


# --- /MAT/LAW15 ------------------------------------------------------
@dataclass
class MatLaw15(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW15` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW15"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW16 ------------------------------------------------------
@dataclass
class MatLaw16(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW16` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW16"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW18 ------------------------------------------------------
@dataclass
class MatLaw18(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW18` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW18"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW19 ------------------------------------------------------
@dataclass
class MatLaw19(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW19` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW19"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW20 ------------------------------------------------------
@dataclass
class MatLaw20(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW20` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW20"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
