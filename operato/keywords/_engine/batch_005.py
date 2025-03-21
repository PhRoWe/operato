#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /ANIM/SHELL/PHI             /ANIM/SHELL/Restype         /ANIM/SHELL/SIG1H
# /ANIM/SHELL/SIG2H           /ANIM/SHELL/TDEL            /ANIM/SHELL/TENS
# /ANIM/TITLE                 /ANIM/VECT                  /ANIM/VERS
#


# --- /ANIM/SHELL/PHI ------------------------------------------------------
@dataclass
class AnimShellPhi(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/ANIM/SHELL/PHI` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/PHI"

    @property
    def pre_conditions(self):

        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/SHELL/Restype ------------------------------------------------------
@dataclass
class AnimShellRestype(Keyword):
    eltype: str
    restype: str
    keyword4: str | None = None

    @property
    def keyword(self):
        if self.keyword4 is not None:
            return f"/ANIM/{self.eltype}/{self.restype}/{self.keyword4}"
        else:
            return f"/ANIM/{self.eltype}/{self.restype}"

    @property
    def pre_conditions(self):
        eltype_pos = ["ELEM", "SHELL"]
        restype_pos = [
            "AMS",
            "DAM1",
            "DAM2",
            "DAM3",
            "/DAMG",
            "DENS",
            "DT",
            "EINT",
            "ENER",
            "EPSD",
            "EPSP",
            "ERROR/THICK",
            "FAIL",
            "HOURG",
            "/NL_EPSD",
            "/NL_EPSP",
            "OFF",
            "P",
            "PHI/N",
            "PHI/ALL",
            "PLY",
            "SIGEQ",
            "SIGX",
            "SIGY",
            "SIGZ",
            "SIGXY",
            "SIGYZ",
            "SIGZX",
            "TEMP",
            "THIC",
            "THIN",
            "TSAIWU",
            "USRi",
            "USRII",
            "USRII/JJ",
            "VONM",
            "/WPLA",
        ]
        return [
            (
                self.eltype in eltype_pos,
                "Unknown element type specified.",
            ),
            (self.restype in restype_pos, "Unknown response type."),
        ]

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/SHELL/SIG1H ------------------------------------------------------
@dataclass
class AnimShellSig1h(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/ANIM/SHELL/SIG1H` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/SIG1H"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/SHELL/SIG2H ------------------------------------------------------
@dataclass
class AnimShellSig2h(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/ANIM/SHELL/SIG2H` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/SIG2H"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/SHELL/TDEL ------------------------------------------------------
@dataclass
class AnimShellTdel(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/ANIM/SHELL/TDEL` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/TDEL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/SHELL/TENS ------------------------------------------------------
@dataclass
class AnimShellTens(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/ANIM/SHELL/TENS` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/SHELL/TENS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/TITLE ------------------------------------------------------
@dataclass
class AnimTitle(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/ANIM/TITLE` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/TITLE"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/VECT ------------------------------------------------------
@dataclass
class AnimVect(Keyword):
    restype: str

    @property
    def keyword(self):
        return f"/ANIM/VECT/{self.restype}"

    @property
    def pre_conditions(self):
        restype_pos = [
            "VEL",
            "DISP",
            "ACC",
            "CONT",
            "CONT/MAX",
            "CONT2",
            "FINT",
            "FEXT",
            "FOPT",
            "PCONT",
            "PCONT2",
            "VROT",
            "DROT",
            "FVEL",
            "FREAC",
            "MREAC",
            "CLUST/FORCE",
            "CLUST/MOM",
        ]
        return [
            (self.restype in restype_pos, "Unknown response type."),
        ]

    @property
    def structure(self):
        structure = []

        return structure


# --- /ANIM/VERS ------------------------------------------------------
@dataclass
class AnimVers(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/ANIM/VERS` is not implemented.")

    @property
    def keyword(self):
        return "/ANIM/VERS"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
