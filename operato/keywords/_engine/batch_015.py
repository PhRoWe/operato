#!/usr/bin/env python3

from dataclasses import dataclass
from typing import List

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPL/LSEARCH/n             /IMPL/MONVOL/OFF            /IMPL/NCYCLE/STOP
# /IMPL/NONLIN/N              /IMPL/NONLIN/SMDISP         /IMPL/NONLIN/SOLVINFO
# /IMPL/PREPAT                /IMPL/PRINT/LINEAR          /IMPL/PRINT/NONLIN
#


# --- /IMPL/LSEARCH/n ------------------------------------------------------
@dataclass
class ImplLsearchN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/LSEARCH/n` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/LSEARCH/n"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/MONVOL/OFF ------------------------------------------------------
@dataclass
class ImplMonvolOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/MONVOL/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/MONVOL/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/NCYCLE/STOP ------------------------------------------------------
@dataclass
class ImplNcycleStop(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/NCYCLE/STOP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/NCYCLE/STOP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/NONLIN/N ------------------------------------------------------
@dataclass
class ImplNonlinN(Keyword):
    """Nonlinear implicit methods.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/impl_nonlin_engine_r.htm)

    """

    N: int
    L_A: int
    Itol: int
    Toli: float | None = 0.0
    Tolj: float | None = 0.0
    Tolk: float | None = 0.0
    line0: str = "#/IMPL/NONLIN/N\n"
    add_header: bool = True

    @property
    def keyword(self):

        return self.line0 + f"/IMPL/NONLIN/{self.N}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [
            IntField("L_A", 1),
            IntField("Itol", 2),
        ]
        if self.Itol in [1, 2, 3]:
            structure.append(FloatField("Toli", 3))
        elif self.Itol in [12, 13, 23]:
            structure.append([FloatField("Toli", 3), FloatField("Toli", 5)])
        elif self.Itol == 123:
            structure.append(
                [FloatField("Toli", 3), FloatField("Tolj", 5), FloatField("Tolk", 7)]
            )
        structure = structure
        return structure


# --- /IMPL/NONLIN/SMDISP ------------------------------------------------------
@dataclass
class ImplNonlinSmdisp(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/NONLIN/SMDISP` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/NONLIN/SMDISP"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/NONLIN/SOLVINFO ------------------------------------------------------
@dataclass
class ImplNonlinSolvinfo(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/NONLIN/SOLVINFO` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/NONLIN/SOLVINFO"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/PREPAT ------------------------------------------------------
@dataclass
class ImplPrepat(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/PREPAT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/PREPAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/PRINT/LINEAR ------------------------------------------------------
@dataclass
class ImplPrintLinear(Keyword):
    """Printout frequency for linear solvers.This keyword is mainly used for iterative
    solver. When a direct solver has been used, only relative residual will print out
    and only in case of linear analysis."""

    n_print: int
    """Printout frequency for linear solvers (works also in nonlinear analysis but 
    rather as debug uses).
    """

    @property
    def keyword(self):
        return f"/IMPL/PRINT/LINEAR/{self.n_print}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/PRINT/NONLIN ------------------------------------------------------
@dataclass
class ImplPrintNonlin(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/PRINT/NONLIN` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/PRINT/NONLIN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
