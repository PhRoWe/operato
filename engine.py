#!/usr/bin/env python3
"""Provides a low-level interface for generating OpenRadioss starter files.

"""
from datetime import datetime
import os
from pathlib import Path
from operato.constants import LINE_SEPARATOR

from operato.keywords.common import Keyword
from operato.keywords.engine import Run


class Engine:
    """Represents the engine part of an OpenRadioss simulation. It features a
    very natural syntax for selecting keyword templates and providing them with
    the parameters they need for instantation:

    """

    def __init__(self, add_header=True, add_separator=False, runname=""):
        """Initializes a new starter instance."""

        self.add_header = add_header
        self.add_separator = add_separator
        self._keywords = []
        self._runname = runname

    @property
    def runname(self) -> str:
        return self._runname

    def add(self, keyword: Keyword) -> None:
        if not isinstance(keyword, Keyword):
            raise ValueError(
                "Argument `keyword` must be an instance of a subclass of `Keyword`"
            )
        if isinstance(keyword, Run):
            self._runname = keyword.runname
        self._keywords.append(keyword)

    def write(
        self, index=1, folder: str | Path | None = None, assume_yes=False
    ) -> None:
        """Writes the keywords to a file.
        "assume_yes"=True does not ask whether existing files should be overwritten
        """
        if folder is None:
            folder = Path().cwd()
        elif isinstance(folder, str):
            folder = Path(folder)

        filepath = folder.joinpath(f"{self.runname}_{index:04d}.rad")
        if not folder.is_dir():
            os.mkdir(folder)
        if filepath.is_file() and not assume_yes:
            overwrite_file = input(
                f"File `{filepath.name}` already exists. Overwrite? [yes/no (default=no)] "
            )

            if not overwrite_file.lower() in ("y", "yes"):
                return
        # Serialize the keywords
        with open(filepath, "w") as fd:
            if self.add_header:
                now = datetime.now().isoformat()
                fd.write("#\n")
                fd.write(f"# File created at {now}\n")
                fd.write("#\n")

            for keyword in self._keywords:
                if self.add_separator:
                    fd.write(LINE_SEPARATOR)
                    fd.write("\n")
                if hasattr(keyword, "add_separator") and keyword.add_separator == True:
                    fd.write(LINE_SEPARATOR)
                    fd.write("\n")

                keyword.write(fd)


if __name__ == "__main__":
    pass
