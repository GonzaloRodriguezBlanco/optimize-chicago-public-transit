from enum import Enum


class CompressionType(Enum):
    UNCOMPRESSED = 'uncompressed'
    GZIP = 'gzip'
    SNAPPY = 'snappy'
    LZ4 = 'lz4'
    ZSTD = 'zstd'
    PRODUCER = 'producer'
