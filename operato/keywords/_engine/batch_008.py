#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import (
    FloatField,
    IntField,
    Keyword,
    StringField,
    ArrayOfAtomicFields,
)
from ...constants import UNKNOWN_INPUT, UNKNOWN_OPT

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /DT/ALE                     /DT/AMS                     /DT/CST_AMS
# /DT/Eltyp/Keyword3/Iflag    /DT/FVMBAG/Iflag            /DT/INTER/Keyword3/Iflag
# /DT/NODA/Keyword3/Iflag     /DT/SHNOD/Keyword3          /DT/SPHCEL/Keyword3
#


# --- /DT/ALE ------------------------------------------------------
@dataclass
class DtAle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/DT/ALE` is not implemented.")

    @property
    def keyword(self):
        return "/DT/ALE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT/AMS ------------------------------------------------------
@dataclass
class DtAms(Keyword):
    """ "Time step control for Advanced Mass Scaling. Advanced Mass Scaling is an
    elementary time step method that increases the time step to a higher value than the
    usual elementary or nodal time step.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/dt_ams_engine_r.htm)"""

    dTmin: float
    dT_sca: float = 0.9
    Iflag: int | None = None
    Tol_AMS: float | None = None
    Niter: int | None = None
    Nprint: int | None = None
    # added commentary line for readability of input deck
    line0: str = "#/DT/AMS/Iflag\n"
    line1: str = (
        "#------------dT_sca|-------------dT_min|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line2: str = (
        "#-----------Tol_AMS|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )
    line3: str = (
        "#--N_iter|--N_print|----3----|----4----|----5----|----6----|----7----|----8----|----9----|----10---|"
    )

    @property
    def keyword(self):
        return self.line0 + f"/DT/AMS/{self.Iflag}"

    @property
    def pre_conditions(self):
        conditions = []
        if self.Iflag == 0:
            conditions.append(
                [
                    (self.dT_sca is not None, UNKNOWN_INPUT + "dT_sca"),
                    (self.dTmin is not None, UNKNOWN_INPUT + "dTmin"),
                ]
            )
        elif self.Iflag == 1 or self.Iflag == 2:
            conditions.append(
                (
                    self.Tol_AMS is not None,
                    UNKNOWN_INPUT + "Tol_AMS",
                )
            )
        elif self.Iflag == 2:
            conditions.append(
                [
                    (self.Niter is not None, UNKNOWN_INPUT + "Niter"),
                    (self.Nprint is not None, UNKNOWN_INPUT + "Nprint"),
                ]
            )
        return []

    @property
    def structure(self):
        structure = []
        if self.Iflag == 0:
            structure.append(StringField("line1", 1, 10))
            structure.append(
                [FloatField("dT_sca", 1), FloatField("dTmin", 3)],
            )
        if self.Iflag == 1 or self.Iflag == 2:
            structure.append(StringField("line2", 1, 10))
            structure.append(FloatField("Tol_AMS", 1))
        if self.Iflag == 2:
            structure.append(StringField("line3", 1, 10))
            structure.append(
                [FloatField("Niter", 1), FloatField("Nprint", 3)],
            )

        return structure


# --- /DT/CST_AMS ------------------------------------------------------
@dataclass
class DtCstAms(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/DT/CST_AMS` is not implemented.")

    @property
    def keyword(self):
        return "/DT/CST_AMS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT/Eltyp/Keyword3/Iflag ------------------------------------------------------
@dataclass
class DtEltypKeyword3Iflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError(
            "Keyword `/DT/Eltyp/Keyword3/Iflag` is not implemented."
        )

    @property
    def keyword(self):
        return "/DT/Eltyp/Keyword3/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT/FVMBAG/Iflag ------------------------------------------------------
@dataclass
class DtFvmbagIflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DT/FVMBAG/Iflag` is not implemented.")

    @property
    def keyword(self):
        return "/DT/FVMBAG/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT/INTER/Keyword3/Iflag ------------------------------------------------------
@dataclass
class DtInterKeyword3Iflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError(
            "Keyword `/DT/INTER/Keyword3/Iflag` is not implemented."
        )

    @property
    def keyword(self):
        return "/DT/INTER/Keyword3/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT/NODA/Keyword3/Iflag ------------------------------------------------------
@dataclass
class DtNodaKeyword3Iflag(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError(
            "Keyword `/DT/NODA/Keyword3/Iflag` is not implemented."
        )

    @property
    def keyword(self):
        return "/DT/NODA/Keyword3/Iflag"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT/SHNOD/Keyword3 ------------------------------------------------------
@dataclass
class DtShnodKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DT/SHNOD/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/DT/SHNOD/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /DT/SPHCEL/Keyword3 ------------------------------------------------------
@dataclass
class DtSphcelKeyword3(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/DT/SPHCEL/Keyword3` is not implemented.")

    @property
    def keyword(self):
        return "/DT/SPHCEL/Keyword3"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
