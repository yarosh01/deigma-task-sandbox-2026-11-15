"""Paging for the list endpoints.

A listing is already in order when it gets here; this module only cuts one page out of it.
"""

from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

from config.settings import DEFAULT_PER_PAGE, MAX_PER_PAGE

T = TypeVar("T")


def clamp_per_page(per_page: int) -> int:
    """The page size actually used: at least 1, at most MAX_PER_PAGE."""
    return max(1, min(per_page, MAX_PER_PAGE))


def paginate(items: Sequence[T], page: int, per_page: int = DEFAULT_PER_PAGE) -> list[T]:
    """The items on one page of an ordered listing. Pages count from 1."""
    if page < 1:
        raise ValueError("pages start at 1")
    per_page = clamp_per_page(per_page)

    start = (page - 1) * per_page
    return list(items[start : start + per_page])
