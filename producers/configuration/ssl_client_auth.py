from enum import Enum


class SslClientAuth(Enum):
    REQUIRED = 'required'
    REQUESTED = 'requested'
    NONE = 'none'
