#!/usr/bin/env python3

from dataclasses import dataclass

from operato.keywords.common import FloatField, IntField, Keyword, StringField

# === Concrete keyword definitions (in alphabetical order) ====================================
#
# /PRINT                      /RAD2RAD/ON                 /RBODY
# /REPORT                     /RERUN                      /RFILE/OFF
# /RFILE/n                    /RUN                        /SHSUB
#


# --- /PRINT ------------------------------------------------------
@dataclass
class Print(Keyword):
    """Sets printout frequency for output file.
    (https://help.altair.com/hwsolvers/rad/topics/solvers/rad/print_engine_r.htm)
    """

    n_print: int = -1000
    n_line: int | None = None
    # added line for readability
    line0: str = "#/PRINT/Nprint(/N_line)\n"
    add_header: bool = False

    @property
    def keyword(self):
        if self.n_line == None:
            return self.line0 + f"/PRINT/{self.n_print}"
        elif self.n_line != None:
            return self.line0 + f"/PRINT/{self.n_print}/{self.n_line}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /RAD2RAD/ON ------------------------------------------------------
@dataclass
class Rad2radOn(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/RAD2RAD/ON` is not implemented.")

    @property
    def keyword(self):
        return "/RAD2RAD/ON"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /RBODY ------------------------------------------------------
@dataclass
class Rbody(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/RBODY` is not implemented.")

    @property
    def keyword(self):
        return "/RBODY"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /REPORT ------------------------------------------------------
@dataclass
class Report(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/REPORT` is not implemented.")

    @property
    def keyword(self):
        return "/REPORT"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /RERUN ------------------------------------------------------
@dataclass
class Rerun(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/RERUN` is not implemented.")

    @property
    def keyword(self):
        return "/RERUN"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /RFILE/OFF ------------------------------------------------------
@dataclass
class RfileOff(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/RFILE/OFF` is not implemented.")

    @property
    def keyword(self):
        return "/RFILE/OFF"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /RFILE/n ------------------------------------------------------
@dataclass
class RfileN(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raiseNotImplementedError("Keyword `/RFILE/n` is not implemented.")

    @property
    def keyword(self):
        return "/RFILE/n"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure


# --- /RUN ------------------------------------------------------
@dataclass
class Run(Keyword):
    runname: str
    run_num: int
    t_stop: float
    restart_letter: str | None = None
    add_header: bool = False

    @property
    def keyword(self):
        if self.restart_letter is not None:
            return f"/RUN/{self.runname}/{self.run_num}/{self.restart_letter}"
        else:
            return f"/RUN/{self.runname}/{self.run_num}"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = [FloatField("t_stop", 1)]

        return structure


# --- /SHSUB ------------------------------------------------------
@dataclass
class Shsub(Keyword):
    attr1: int
    attr2: float

    def __post_init__(self):
        # TODO: Implementation
        raise NotImplementedError("Keyword `/SHSUB` is not implemented.")

    @property
    def keyword(self):
        return "/SHSUB"

    @property
    def pre_conditions(self):
        return []

    @property
    def structure(self):
        structure = []

        return structure
