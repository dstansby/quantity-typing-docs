from .version import version as __version__

from typing import Annotated

__all__ = ["deg2rad"]

class A:
    def __class_getitem__(cls, t: type):
        return Annotated[cls, t]


def deg2rad(arg: A[str]) -> A[bytes]:
    return A()
