from enum import Enum


class SslProtocol(Enum):
    TLS_V_1_2 = 'TLSv1.2'
    TLS_V_1_3 = 'TLSv1.3'
    TLS = 'TLS'  # discouraged due to known security vulnerabilities
    TLS_V_1_1 = 'TLSv1.1'  # discouraged due to known security vulnerabilities
    SSL = 'SSL'  # discouraged due to known security vulnerabilities
    SSL_V_2 = 'SSLv2'  # discouraged due to known security vulnerabilities
    SSL_V_3 = 'SSLv3'  # discouraged due to known security vulnerabilities
