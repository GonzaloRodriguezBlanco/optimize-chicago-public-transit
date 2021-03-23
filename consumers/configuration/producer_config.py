from enum import Enum


class ProducerConfig(Enum):
    ACKS = 'acks'
    BATCH_SIZE = 'batch.size'
    BUFFER_MEMORY = 'buffer.memory'
    DELIVERY_TIMEOUT_MS = 'delivery.timeout.ms'
    ENABLE_IDEMPOTENCE = 'enable.idempotence'
    KEY_SERIALIZER = 'key.serializer'
    LINGER_MS = 'linger.ms'
    MAX_BLOCK_MS = 'max.block.ms'
    MAX_IN_FLIGHT_REQUESTS_PER_CONNECTION = 'max.in.flight.requests.per.connection'
    MAX_REQUEST_SIZE = 'max.request.size'
    METADATA_MAX_IDLE_MS = 'metadata.max.idle.ms'
    PARTITIONER_CLASS = 'partitioner.class'
    TRANSACTIONAL_ID = 'transactional.id'
    TRANSACTION_TIMEOUT_MS = 'transaction.timeout.ms'
    VALUE_SERIALIZER = 'value.serializer'
