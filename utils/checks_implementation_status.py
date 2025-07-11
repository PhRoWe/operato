from typing import List, Type
from operato.keywords.common import Keyword  # Replace with the correct import
import os


def get_all_subclasses(cls: Type) -> List[Type]:
    """Recursively gather all subclasses of a class."""
    subclasses = set()
    work = [cls]
    while work:
        parent = work.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                work.append(child)
    return list(subclasses)


def is_implemented(subclass: Type, parent: Type) -> bool:
    """Check if subclass uses the parent's __post_init__"""
    sub_post = getattr(subclass, "__post_init__", None)
    par_post = getattr(parent, "__post_init__", None)
    return sub_post == par_post


def classify_subclasses():
    all_subs = get_all_subclasses(Keyword)
    implemented = []
    not_implemented = []

    for cls in all_subs:
        if is_implemented(cls, Keyword):
            implemented.append(cls.__name__)
        else:
            not_implemented.append(cls.__name__)

    return implemented, not_implemented


def save_to_file(filename: str, implemented: List[str], not_implemented: List[str]):
    with open(filename, "w") as f:
        f.write("Implemented classes:\n")
        for cls in sorted(implemented):
            f.write(f" - {cls}\n")

        f.write("\nNot implemented classes:\n")
        for cls in sorted(not_implemented):
            f.write(f" - {cls}\n")


if __name__ == "__main__":
    # For Engine keywords:
    # from operato.keywords.engine import keywords

    # impl, not_impl = classify_subclasses()
    # save_to_file("Engine_keywords_implementation_status.txt", impl, not_impl)
    from operato.keywords.starter import keywords

    impl, not_impl = classify_subclasses()
    save_to_file("Starter_keywords_implementation_status.txt", impl, not_impl)
