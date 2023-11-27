from .version import version as __version__
import astropy.units as u

__all__ = ["deg2rad"]


def deg2rad(deg: u.Quantity[u.deg]) -> u.Quantity[u.rad]:
    return deg.to(u.rad)
