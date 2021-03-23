from enum import Enum


class ConsumerConfig(Enum):
    ALLOW_AUTO_CREATE_TOPICS = 'allow.auto.create.topics'
    AUTO_COMMIT_INTERVAL_MS = 'auto.commit.interval.ms'
    AUTO_OFFSET_RESET = 'auto.offset.reset'
    CHECK_CRCS = 'check.crcs'
    CLIENT_RACK = 'client.rack'
    ENABLE_AUTO_COMMIT = 'enable.auto.commit'
    EXCLUDE_INTERNAL_TOPICS = 'exclude.internal.topics'
    FETCH_MAX_WAIT_MS = 'fetch.max.wait.ms'
    FETCH_MIN_BYTES = 'fetch.min.bytes'
    GROUP_ID = 'group.id'
    GROUP_INSTANCE_ID = 'group.instance.id'
    HEARTBEAT_INTERVAL_MS = 'heartbeat.interval.ms'
    ISOLATION_LEVEL = 'isolation.level'
    KEY_DESERIALIZER = 'key.deserializer'
    MAX_PARTITION_FETCH_BYTES = 'max.partition.fetch.bytes'
    MAX_POLL_INTERVAL_MS = 'max.poll.interval.ms'
    MAX_POLL_RECORDS = 'max.poll.records'
    PARTITION_ASSIGNMENT_STRATEGY = 'partition.assignment.strategy'
    SESSION_TIMEOUT_MS = 'session.timeout.ms'
    VALUE_DESERIALIZER = 'value.deserializer'
