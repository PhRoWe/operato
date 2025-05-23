#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /IMPL/SBCS/OUTCORE          /IMPL/SHPOFF                /IMPL/SHPON
# /IMPL/SINIT                 /IMPL/SOLVER                /IMPL/SPRBACK
# /IMPL/SPRING                /INIV/AXIS                  /INIV/AXIS/Keyword3/1
#


# --- /IMPL/SBCS/OUTCORE ------------------------------------------------------
@dataclass
class ImplSbcsOutcore(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/SBCS/OUTCORE` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SBCS/OUTCORE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/SHPOFF ------------------------------------------------------
@dataclass
class ImplShpoff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/SHPOFF` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SHPOFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/SHPON ------------------------------------------------------
@dataclass
class ImplShpon(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/SHPON` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SHPON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/SINIT ------------------------------------------------------
@dataclass
class ImplSinit(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/IMPL/SINIT` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SINIT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/SOLVER ------------------------------------------------------
@dataclass
class ImplSolver(Keyword):
    """Selects linear solver.
    (https://2022.help.altair.com/2022.2/hwsolvers/rad/topics/solvers/rad/impl_solver_engine_r.htm)
    """

    i_prec: int
    it_max: int
    i_tol: int
    tol: float
    n: int = 2
    # added line for readability of input deck
    line: str = (
        "#--I_prec|---It_max|--- -Itol|------Tol|----5----|----6----|----7----|----8----|----9----|----10---|"
    )

    @property
    def keyword(self):
        return f"/IMPL/SOLVER/{self.n}"

    @property
    def pre_conditions(self):
        # FIXME: add preconditions according to reference guide
        return []

    @property
    def structure(self):
        structure = [
            StringField("line", 1, 10),
            [
                IntField("i_prec", 1),
                IntField("it_max", 2),
                IntField("i_tol", 3),
                FloatField("tol", 4),
            ],
        ]

        return structure


# --- /IMPL/SPRBACK ------------------------------------------------------
@dataclass
class ImplSprback(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/SPRBACK` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SPRBACK"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /IMPL/SPRING ------------------------------------------------------
@dataclass
class ImplSpring(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/IMPL/SPRING` is not implemented.")

    @property
    def keyword(self):
        return "/IMPL/SPRING"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIV/AXIS ------------------------------------------------------
@dataclass
class InivAxis(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIV/AXIS` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/AXIS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /INIV/AXIS/Keyword3/1 ------------------------------------------------------
@dataclass
class InivAxisKeyword31(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/INIV/AXIS/Keyword3/1` is not implemented.")

    @property
    def keyword(self):
        return "/INIV/AXIS/Keyword3/1"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
