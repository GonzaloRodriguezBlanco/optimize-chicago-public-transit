from enum import Enum


class IsolationLevel(Enum):
    READ_COMMITTED = 'read_committed'
    READ_UNCOMMITTED = 'read_uncommitted'
