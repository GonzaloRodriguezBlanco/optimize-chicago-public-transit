from enum import Enum


class ClientDnsLookup(Enum):
    DEFAULT = 'default'
    USE_ALL_DNS_IPS = 'use_all_dns_ips'
    RESOLVE_CANONICAL_BOOTSTRAP_SERVERS_ONLY = 'resolve_canonical_bootstrap_servers_only'
