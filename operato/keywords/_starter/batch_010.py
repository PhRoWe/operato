#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /EREF                       /EULER/MAT                  /FAIL
# /FAIL/ALTER                 /FAIL/BIQUAD                /FAIL/CHANG
# /FAIL/COCKCROFT             /FAIL/CONNECT               /FAIL/EMC
#


# --- /EREF ------------------------------------------------------
@dataclass
class Eref(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EREF` is not implemented.")

    @property
    def keyword(self):
        return "/EREF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /EULER/MAT ------------------------------------------------------
@dataclass
class EulerMat(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/EULER/MAT` is not implemented.")

    @property
    def keyword(self):
        return "/EULER/MAT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FAIL ------------------------------------------------------
@dataclass
class Fail(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FAIL` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FAIL/ALTER ------------------------------------------------------
@dataclass
class FailAlter(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FAIL/ALTER` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/ALTER"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FAIL/BIQUAD ------------------------------------------------------
@dataclass
class FailBiquad(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FAIL/BIQUAD` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/BIQUAD"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FAIL/CHANG ------------------------------------------------------
@dataclass
class FailChang(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FAIL/CHANG` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/CHANG"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FAIL/COCKCROFT ------------------------------------------------------
@dataclass
class FailCockcroft(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FAIL/COCKCROFT` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/COCKCROFT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FAIL/CONNECT ------------------------------------------------------
@dataclass
class FailConnect(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/FAIL/CONNECT` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/CONNECT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /FAIL/EMC ------------------------------------------------------
@dataclass
class FailEmc(Keyword):
    attr1: int
    attr2: float
    add_header: bool = True

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/FAIL/EMC` is not implemented.")

    @property
    def keyword(self):
        return "/FAIL/EMC"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
