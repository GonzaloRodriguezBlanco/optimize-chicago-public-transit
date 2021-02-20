from enum import Enum


class SecurityProtocol(Enum):
    PLAINTEXT = 'PLAINTEXT'
    SSL = 'SSL'
    SASL_PLAINTEXT = 'SASL_PLAINTEXT'
    SASL_SSL = 'SASL_SSL'
