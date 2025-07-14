#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    match_type_append_line_struct,
)

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /MAT/LAW21                  /MAT/LAW22                  /MAT/LAW23
# /MAT/LAW24                  /MAT/LAW25                  /MAT/LAW26
# /MAT/LAW27                  /MAT/LAW28                  /MAT/LAW32
#


# --- /MAT/LAW21 ------------------------------------------------------
@dataclass
class MatLaw21(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MAT/LAW21` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW21"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW22 ------------------------------------------------------
@dataclass
class MatLaw22(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MAT/LAW22` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW22"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW23 ------------------------------------------------------
@dataclass
class MatLaw23(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MAT/LAW23` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW23"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW24 ------------------------------------------------------
@dataclass
class MatLaw24(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MAT/LAW24` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW24"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW25 ------------------------------------------------------
@dataclass
class MatLaw25(Keyword):
    """This law describes the composite shell and solid material using the Tsai-Wu formulation.

    The material is assumed to be orthotropic-elastic before the Tsai-Wu criterion is
    reached. The material becomes nonlinear afterwards. For solid elements, the material
      is assumed to be linearly elastic in the transverse direction. The Tsai-Wu
      criterion limit can be set dependent on the plastic work and strain rate to model
      material hardening. Strain and plastic energy criterion for brittle damage and
      failure are available. A simplified delamination criterion based on out-of-plane
      shear angle can be used.

      https://help.altair.com/hwsolvers/rad/topics/solvers/rad/tsai_wu_formulation_starter_r.htm
    """

    # NON-DEFAULTS:
    mat_id: int
    rho: float
    E11: float
    E22: float
    E33: float
    nu12: float
    G12: float
    G13: float
    G23: float
    i_off: int
    depsdt0: float
    # DEFAULTS:
    mat_title: str = ""
    unit_id: int | None = None
    i_form: int | None = None
    eps_f1: float | None = None
    eps_f2: float | None = None
    eps_t1: float | None = None
    eps_m1: float | None = None
    eps_t2: float | None = None
    eps_m2: float | None = None
    d_max: float | None = None
    W_p_max: float | None = None
    W_p_ref: float | None = None
    Ratio: float | None = None
    b: float | None = None
    n: float | None = None
    f_max: float | None = None
    sig_1y_t: float | None = None
    sig_2y_t: float | None = None
    sig_1y_c: float | None = None
    sig_2y_c: float | None = None
    sig_12y_t: float | None = None
    sig_12y_c: float | None = None
    alpha: float | None = None
    c: float | None = None
    ICC: int | None = None
    gamma_ini: float | None = None
    gamma_max: float | None = None
    d_3max: float | None = None
    F_smooth: int | None = None
    F_cut: float | None = None
    add_header: bool = True

    @property
    def keyword(self):
        line0 = "#/MAT/LAW25/mat_ID(/unit_id)\n"
        line = f"/MAT/LAW25/{self.mat_id}"
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
        #
        structure.append(
            [
                FloatField("E11", 1),
                FloatField("E22", 3),
                FloatField("nu12", 5),
                IntField("i_form", 7),
                FloatField("E33", 9),
            ]
        )
        # line3
        substructure = []
        for i, attr in enumerate(["G12", "G23", "G13", "eps_f1", "eps_f2"]):
            substructure.append(FloatField(attr, 2 * i + 1))
        structure.append(substructure)
        # line4
        structure = match_type_append_line_struct(
            self, structure, ["eps_t1", "eps_m1", "eps_t2", "eps_m2", "d_max"]
        )
        if self.i_form == 0 or type(self.i_form) == None:
            # Composite Plasticity Hardening
            structure = match_type_append_line_struct(
                self, structure, ["W_p_max", "W_p_ref", "i_off", "-" "Ratio"]
            )
            structure = match_type_append_line_struct(
                self, structure, ["b", "n", "f_max"]
            )
            # Composite Yield Stress in Tension Compression
            structure = match_type_append_line_struct(
                self,
                structure,
                ["sig_1y_t", "sig_2y_t", "sig_1y_c", "sig_2y_c", "alpha"],
            )
            # Yield Stress in Shear and Strain Rate
            structure = match_type_append_line_struct(
                self, structure, ["sig_12y_c", "sig_12y_t", "c", "depsdt0", "ICC"]
            )

        elif self.i_form == 1:
            # Composite Plasticity Hardening
            structure.append(
                [
                    FloatField("W_p_max", 1),
                    IntField("i_off", 5),
                    IntField("WP_fail", 6),
                    FloatField("Ratio", 7),
                ]
            )
            # Global Composite Plasticity Parameters
            structure = match_type_append_line_struct(
                self, structure, ["c", "depsdt_0", "alpha", "---", "ICC_global"]
            )
            # Composite Plasticity in Tension Directions 1 and 2
            structure = match_type_append_line_struct(
                self, structure, ["sig_1y_t", "b_1_t", "n_1_t", "sig_1max_t", "c_1_t"]
            )
            # line8
            structure = match_type_append_line_struct(
                self, structure, ["eps_1_t1", "eps_1_t2", "sig_1rs_t", "W_1p_maxt"]
            )
            # line9
            structure = match_type_append_line_struct(
                self, structure, ["sig_2y_t", "b_2_t", "n_2_t", "sig_2max_t", "c_2_t"]
            )
            # line10
            structure = match_type_append_line_struct(
                self, structure, ["eps_2_t1", "eps_2_t2", "sig_2rs_t", "W_2p_maxt"]
            )
            # Composite Plasticity in Compression Directions 1 and 2
            # line11
            structure = match_type_append_line_struct(
                self, structure, ["sig_1y_c", "b_1_c", "n_1_c", "sig_1max_c", "c_1_c"]
            )
            # line12
            structure = match_type_append_line_struct(
                self, structure, ["eps_1_c1", "eps_1_c2", "sig_1rs_c", "W_1p_maxc"]
            )
            # line13
            structure = match_type_append_line_struct(
                self, structure, ["sig_2y_c", "b_2_c", "n_2_c", "sig_2max_c", "c_2_c"]
            )
            # line14
            structure = match_type_append_line_struct(
                self, structure, ["eps_2_c1", "eps_2_c2", "sig_2rs_c", "W_2p_maxc"]
            )
            # Composite Plasticity in Shear
            # line15
            structure = match_type_append_line_struct(
                self, structure, ["sig_12y", "b_12", "n_12", "sig_12max", "c_12"]
            )
            # line16
            structure = match_type_append_line_struct(
                self, structure, ["eps_12_1", "eps_12_2", "sig_12rs", "W_12p_max"]
            )
        # Delamination
        structure = match_type_append_line_struct(
            self, structure, ["gamma_ini", "gamma_max", "d_3max"]
        )
        # Strain Rate Filtering
        structure = match_type_append_line_struct(
            self, structure, ["F_cut", "F_smooth"]
        )
        return structure


# --- /MAT/LAW26 ------------------------------------------------------
@dataclass
class MatLaw26(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MAT/LAW26` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW26"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW27 ------------------------------------------------------
@dataclass
class MatLaw27(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MAT/LAW27` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW27"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW28 ------------------------------------------------------
@dataclass
class MatLaw28(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/MAT/LAW28` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW28"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /MAT/LAW32 ------------------------------------------------------
@dataclass
class MatLaw32(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/MAT/LAW32` is not implemented.")

    @property
    def keyword(self):
        return "/MAT/LAW32"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
