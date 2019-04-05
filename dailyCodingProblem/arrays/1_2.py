# -*- coding: utf-8 -*-

from typing import List, Tuple


def windows_to_be_sorted(arr: List[int]) -> List[Tuple[int, int]]:
    """Take an array and return the windows to sort."""
    # need to compare sequential list elements,
    # so need to zip list w/ an offset of itself
    zipped_list = zip(arr[:-1], arr[1:])
    zipped_list = enumerate(zipped_list)

    candidate_starts = (
        filter(lambda entry: entry[1][0] > entry[1][1], zipped_list)
    )

    candidate_starts = list(candidate_starts)

    candidate_regions = []

    for (index, entry) in enumerate(arr):
        if index > candidate_starts[0][0]:
            if entry > candidate_starts[0][1][0]:
                candidate_regions.append(
                    (candidate_starts[0][0], index-1),
                )
                candidate_starts.pop(0)

    return candidate_regions
