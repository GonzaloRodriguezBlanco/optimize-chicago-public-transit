from enum import Enum


class AutoOffsetReset(Enum):
    LATEST = 'latest'
    EARLIEST = 'earliest'
    NONE = 'none'
