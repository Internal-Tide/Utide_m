import pkg_resources

from ._reconstruct import reconstruct
from ._solve import solve,solve_m
from ._ut_constants import (
    constit_index_dict,
    cycles_per_hour,
    hours_per_cycle,
    ut_constants,
)


try:
    __version__ = pkg_resources.get_distribution("utide").version
except Exception:
    __version__ = "unknown"

__all__ = [
    "solve",
    "solve_m",
    "reconstruct",
    "ut_constants",
    "constit_index_dict",
    "hours_per_cycle",
    "cycles_per_hour",
]
