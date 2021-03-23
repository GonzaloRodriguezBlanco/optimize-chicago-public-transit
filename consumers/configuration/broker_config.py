from enum import Enum


class BrokerConfig(Enum):
    ADVERTISED_HOST_NAME = 'advertised.host.name'  # DEPRECATED use advertised.listeners
    ADVERTISED_LISTENERS = 'advertised.listeners'
    ADVERTISED_PORT = 'advertised.port'  # DEPRECATED use advertised.listeners
    ALTER_CONFIG_POLICY_CLASS_NAME = 'alter.config.policy.class.name'
    ALTER_LOG_DIRS_REPLICATION_QUOTA_WINDOW_NUM = 'alter.log.dirs.replication.quota.window.num'
    ALTER_LOG_DIRS_REPLICATION_QUOTA_WINDOW_SIZE_SECONDS = 'alter.log.dirs.replication.quota.window.size.seconds'
    AUTHORIZER_CLASS_NAME = 'authorizer.class.name'
    AUTO_CREATE_TOPICS_ENABLE = 'auto.create.topics.enable'
    AUTO_LEADER_REBALANCE_ENABLE = 'auto.leader.rebalance.enable'
    BACKGROUND_THREADS = 'background.threads'
    BROKER_ID = 'broker.id'
    BROKER_ID_GENERATION_ENABLE = 'broker.id.generation.enable'
    BROKER_RACK = 'broker.rack'
    CLIENT_QUOTA_CALLBACK_CLASS = 'client.quota.callback.class'
    CONNECTIONS_MAX_REAUTH_MS = 'connections.max.reauth.ms'
    CONNECTION_FAILED_AUTHENTICATION_DELAY_MS = 'connection.failed.authentication.delay.ms'
    CONTROLLED_SHUTDOWN_ENABLE = 'controlled.shutdown.enable'
    CONTROLLED_SHUTDOWN_MAX_RETRIES = 'controlled.shutdown.max.retries'
    CONTROLLED_SHUTDOWN_RETRY_BACKOFF_MS = 'controlled.shutdown.retry.backoff.ms'
    CONTROLLED_SOCKET_TIMEOUT_MS = 'controller.socket.timeout.ms'
    CONTROLLER_QUOTA_WINDOW_NUM = 'controller.quota.window.num'
    CONTROLLER_QUOTA_WINDOW_SIZE_SECONDS = 'controller.quota.window.size.seconds'
    CONTROL_PLANE_LISTENER_NAME = 'control.plane.listener.name'
    CREATE_TOPIC_POLICY_CLASS_NAME = 'create.topic.policy.class.name'
    DEFAULT_REPLICATION_FACTOR = 'default.replication.factor'
    DELEGATION_TOKEN_EXPIRY_CHECK_INTERVAL_MS = 'delegation.token.expiry.check.interval.ms'
    DELEGATION_TOKEN_EXPIRY_TIME_MS = 'delegation.token.expiry.time.ms'
    DELEGATION_TOKEN_MASTER_KEY = 'delegation.token.master.key'
    DELEGATION_TOKEN_MAX_LIFETIME_MS = 'delegation.token.max.lifetime.ms'
    DELETE_RECORDS_PURGATORY_PURGE_INTERVAL_REQUESTS = 'delete.records.purgatory.purge.interval.requests'
    DELETE_TOPIC_ENABLE = 'delete.topic.enable'
    FETCH_PURGATORY_PURGE_INTERVAL_REQUESTS = 'fetch.purgatory.purge.interval.requests'
    GROUP_INITIAL_REBALANCE_DELAY_MS = 'group.initial.rebalance.delay.ms'
    GROUP_MAX_SESSION_TIMEOUT_MS = 'group.max.session.timeout.ms'
    GROUP_MAX_SIZE = 'group.max.size'
    GROUP_MIN_SESSION_TIMEOUT_MS = 'group.min.session.timeout.ms'
    HOST_NAME = 'host.name'  # DEPRECATED use listeners instead
    INTER_BROKER_LISTENER_NAME = 'inter.broker.listener.name'
    INTER_BROKER_PROTOCOL_VERSION = 'inter.broker.protocol.version'
    KAFKA_METRICS_POLLING_INTERVAL_SECS = 'kafka.metrics.polling.interval.secs'
    KAFKA_METRICS_REPORTERS = 'kafka.metrics.reporters'
    LEADER_IMBALANCE_CHECK_INTERVAL_SECONDS = 'leader.imbalance.check.interval.seconds'
    LEADER_IMBALANCE_PER_BROKER_PERCENTAGE = 'leader.imbalance.per.broker.percentage'
    LISTENERS = 'listeners'
    LISTENER_SECURITY_PROTOCOL_MAP = 'listener.security.protocol.map'
    LOG_CLEANER_BACKOFF_MS = 'log.cleaner.backoff.ms'
    LOG_CLEANER_DEDUPE_BUFFER_SIZE = 'log.cleaner.dedupe.buffer.size'
    LOG_CLEANER_DELETE_RETENTION_MS = 'log.cleaner.delete.retention.ms'
    LOG_CLEANER_ENABLE = 'log.cleaner.enable'
    LOG_CLEANER_IO_BUFFER_LOAD_FACTOR = 'log.cleaner.io.buffer.load.factor'
    LOG_CLEANER_IO_BUFFER_SIZE = 'log.cleaner.io.buffer.size'
    LOG_CLEANER_IO_MAX_BYTES_PER_SECOND = 'log.cleaner.io.max.bytes.per.second'
    LOG_CLEANER_MAX_COMPACTION_LAG_MS = 'log.cleaner.max.compaction.lag.ms'
    LOG_CLEANER_MIN_CLEANABLE_RATIO = 'log.cleaner.min.cleanable.ratio'
    LOG_CLEANER_MIN_COMPACTION_LAG_MS = 'log.cleaner.min.compaction.lag.ms'
    LOG_CLEANER_THREADS = 'log.cleaner.threads'
    LOG_CLEANUP_POLICY = 'log.cleanup.policy'
    LOG_DIR = 'log.dir'
    LOG_DIRS = 'log.dirs'
    LOG_FLUSH_INTERVAL_MESSAGES = 'log.flush.interval.messages'
    LOG_FLUSH_INTERVAL_MS = 'log.flush.interval.ms'
    LOG_FLUSH_OFFSET_CHECKPOINT_INTERVAL_MS = 'log.flush.offset.checkpoint.interval.ms'
    LOG_FLUSH_SCHEDULER_INTERVAL_MS = 'log.flush.scheduler.interval.ms'
    LOG_FLUSH_START_OFFSET_CHECKPOINT_INTERVAL_MS = 'log.flush.start.offset.checkpoint.interval.ms'
    LOG_INDEX_INTERVAL_BYTES = 'log.index.interval.bytes'
    LOG_INDEX_SIZE_MAX_BYTES = 'log.index.size.max.bytes'
    LOG_MESSAGE_DOWNCONVERSION_ENABLE = 'log.message.downconversion.enable'
    LOG_MESSAGE_FORMAT_VERSION = 'log.message.format.version'
    LOG_MESSAGE_TIMESTAMP_DIFFERENCE_MAX_MS = 'log.message.timestamp.difference.max.ms'
    LOG_MESSAGE_TIMESTAMP_TYPE = 'log.message.timestamp.type'
    LOG_PREALLOCATE = 'log.preallocate'
    LOG_RETENTION_BYTES = 'log.retention.bytes'
    LOG_RETENTION_CHECK_INTERVAL_MS = 'log.retention.check.interval.ms'
    LOG_RETENTION_HOURS = 'log.retention.hours'
    LOG_RETENTION_MINUTES = 'log.retention.minutes'
    LOG_RETENTION_MS = 'log.retention.ms'
    LOG_ROLL_HOURS = 'log.roll.hours'
    LOG_ROLL_JITTER_HOURS = 'log.roll.jitter.hours'
    LOG_ROLL_JITTER_MS = 'log.roll.jitter.ms'
    LOG_ROLL_MS = 'log.roll.ms'
    LOG_SEGMENT_BYTES = 'log.segment.bytes'
    LOG_SEGMENT_DELETE_DELAY_MS = 'log.segment.delete.delay.ms'
    MAX_CONNECTIONS = 'max.connections'
    MAX_CONNECTIONS_PER_IP = 'max.connections.per.ip'
    MAX_CONNECTIONS_PER_IP_OVERRIDES = 'max.connections.per.ip.overrides'
    MAX_CONNECTION_CREATION_RATE = 'max.connection.creation.rate'
    MAX_INCREMENTAL_FETCH_SESSION_CACHE_SLOTS = 'max.incremental.fetch.session.cache.slots'
    MESSAGE_MAX_BYTES = 'message.max.bytes'
    NUM_IO_THREADS = 'num.io.threads'
    NUM_NETWORK_THREADS = 'num.network.threads'
    NUM_PARTITIONS = 'num.partitions'
    NUM_RECOVERY_THREADS_PER_DATA_DIR = 'num.recovery.threads.per.data.dir'
    NUM_REPLICA_ALTER_LOG_DIRS_THREADS = 'num.replica.alter.log.dirs.threads'
    NUM_REPLICA_FETCHERS = 'num.replica.fetchers'
    OFFSETS_COMMIT_REQUIRED_ACKS = 'offsets.commit.required.acks'
    OFFSETS_COMMIT_TIMEOUT_MS = 'offsets.commit.timeout.ms'
    OFFSETS_LOAD_BUFFER_SIZE = 'offsets.load.buffer.size'
    OFFSETS_RETENTION_CHECK_INTERVAL_MS = 'offsets.retention.check.interval.ms'
    OFFSETS_RETENTION_MINUTES = 'offsets.retention.minutes'
    OFFSETS_TOPIC_COMPRESSION_CODEC = 'offsets.topic.compression.codec'
    OFFSETS_TOPIC_NUM_PARTITIONS = 'offsets.topic.num.partitions'
    OFFSETS_TOPIC_REPLICATION_FACTOR = 'offsets.topic.replication.factor'
    OFFSETS_TOPIC_SEGMENT_BYTES = 'offsets.topic.segment.bytes'
    OFFSET_METADATA_MAX_BYTES = 'offset.metadata.max.bytes'
    PASSWORD_ENCODER_CIPHER_ALGORITHM = 'password.encoder.cipher.algorithm'
    PASSWORD_ENCODER_ITERATIONS = 'password.encoder.iterations'
    PASSWORD_ENCODER_KEYFACTORY_ALGORITHM = 'password.encoder.keyfactory.algorithm'
    PASSWORD_ENCODER_KEY_LENGTH = 'password.encoder.key.length'
    PASSWORD_ENCODER_OLD_SECRET = 'password.encoder.old.secret'
    PASSWORD_ENCODER_SECRET = 'password.encoder.secret'
    PORT = 'port'  # DEPRECATED use listeners instead
    PRINCIPAL_BUILDER_CLASS = 'principal.builder.class'
    PRODUCER_PURGATORY_PURGE_INTERVAL_REQUESTS = 'producer.purgatory.purge.interval.requests'
    QUEUED_MAX_REQUESTS = 'queued.max.requests'
    QUEUED_MAX_REQUEST_BYTES = 'queued.max.request.bytes'
    QUOTA_CONSUMER_DEFAULT = 'quota.consumer.default'
    QUOTA_PRODUCER_DEFAULT = 'quota.producer.default'
    QUOTA_WINDOW_NUM = 'quota.window.num'
    QUOTA_WINDOW_SIZE_SECONDS = 'quota.window.size.seconds'
    REPLICATION_QUOTA_WINDOW_NUM = 'replication.quota.window.num'
    REPLICATION_QUOTA_WINDOW_SIZE_SECONDS = 'replication.quota.window.size.seconds'
    REPLICA_FETCH_BACKOFF_MS = 'replica.fetch.backoff.ms'
    REPLICA_FETCH_MAX_BYTES = 'replica.fetch.max.bytes'
    REPLICA_FETCH_MIN_BYTES = 'replica.fetch.min.bytes'
    REPLICA_FETCH_RESPONSE_MAX_BYTES = 'replica.fetch.response.max.bytes'
    REPLICA_FETCH_WAIT_MAX_MS = 'replica.fetch.wait.max.ms'
    REPLICA_HIGH_WATERMARK_CHECKPOINT_INTERVAL_MS = 'replica.high.watermark.checkpoint.interval.ms'
    REPLICA_LAG_TIME_MAX_MS = 'replica.lag.time.max.ms'
    REPLICA_SELECTOR_CLASS = 'replica.selector.class'
    REPLICA_SOCKET_RECEIVE_BUFFER_BYTES = 'replica.socket.receive.buffer.bytes'
    REPLICA_SOCKET_TIMEOUT_MS = 'replica.socket.timeout.ms'
    RESERVED_BROKER_MAX_ID = 'reserved.broker.max.id'
    SASL_ENABLED_MECHANISMS = 'sasl.enabled.mechanisms'
    SASL_KERBEROS_PRINCIPAL_TO_LOCAL_RULES = 'sasl.kerberos.principal.to.local.rules'
    SASL_MECHANISM_INTER_BROKER_PROTOCOL = 'sasl.mechanism.inter.broker.protocol'
    SASL_SERVER_CALLBACK_HANDLER_CLASS = 'sasl.server.callback.handler.class'
    SECURITY_INTER_BROKER_PROTOCOL = 'security.inter.broker.protocol'
    SOCKET_RECEIVE_BUFFER_BYTES = 'socket.receive.buffer.bytes'
    SOCKET_REQUEST_MAX_BYTES = 'socket.request.max.bytes'
    SOCKET_SEND_BUFFER = 'socket.send.buffer.bytes'
    SSL_CLIENT_AUTH = 'ssl.client.auth'
    SSL_PRINCIPAL_MAPPING_RULES = 'ssl.principal.mapping.rules'
    TRANSACTIONAL_ID_EXPIRATION_MS = 'transactional.id.expiration.ms'
    TRANSACTION_ABORT_TIMED_OUT_TRANSACTION_CLEANUP_INTERVAL_MS = 'transaction.abort.timed.out.transaction.cleanup.interval.ms' # noqa
    TRANSACTION_MAX_TIMEOUT_MS = 'transaction.max.timeout.ms'
    TRANSACTION_REMOVE_EXPIRED_TRANSACTION_CLEANUP_INTERVAL_MS = 'transaction.remove.expired.transaction.cleanup.interval.ms' # noqa
    TRANSACTION_STATE_LOG_LOAD_BUFFER_SIZE = 'transaction.state.log.load.buffer.size'
    TRANSACTION_STATE_LOG_MIN_ISR = 'transaction.state.log.min.isr'
    TRANSACTION_STATE_LOG_NUM_PARTITIONS = 'transaction.state.log.num.partitions'
    TRANSACTION_STATE_LOG_REPLICATION_FACTOR = 'transaction.state.log.replication.factor'
    TRANSACTION_STATE_LOG_SEGMENT_BYTES = 'transaction.state.log.segment.bytes'
    ZOOKEEPER_CLIENTCNXNSOCKET = 'zookeeper.clientCnxnSocket'
    ZOOKEEPER_CONNECT = 'zookeeper.connect'
    ZOOKEEPER_CONNECTION_TIMEOUT_MS = 'zookeeper.connection.timeout.ms'
    ZOOKEEPER_MAC_IN_FLIGHT_REQUESTS = 'zookeeper.max.in.flight.requests'
    ZOOKEEPER_SESSION_TIMEOUT_MS = 'zookeeper.session.timeout.ms'
    ZOOKEEPER_SET_ACL = 'zookeeper.set.acl'
    ZOOKEEPER_SSL_CIPHER_SUITES = 'zookeeper.ssl.cipher.suites'
    ZOOKEEPER_SSL_CLIENT_ENABLE = 'zookeeper.ssl.client.enable'
    ZOOKEEPER_SSL_CRL_ENABLE = 'zookeeper.ssl.crl.enable'
    ZOOKEEPER_SSL_ENABLED_PROTOCOLS = 'zookeeper.ssl.enabled.protocols'
    ZOOKEEPER_SSL_ENDPOINT_IDENTIFICATION_ALGORITHM = 'zookeeper.ssl.endpoint.identification.algorithm'
    ZOOKEEPER_SSL_KEYSTORE_LOCATION = 'zookeeper.ssl.keystore.location'
    ZOOKEEPER_SSL_KEYSTORE_PASSWORD = 'zookeeper.ssl.keystore.password'
    ZOOKEEPER_SSL_KEYSTORE_TYPE = 'zookeeper.ssl.keystore.type'
    ZOOKEEPER_SSL_OCSP_ENABLE = 'zookeeper.ssl.ocsp.enable'
    ZOOKEEPER_SSL_PROTOCOL = 'zookeeper.ssl.protocol'
    ZOOKEEPER_SSL_TRUSTSTORE_LOCATION = 'zookeeper.ssl.truststore.location'
    ZOOKEEPER_SSL_TRUSTSTORE_PASSWORD = 'zookeeper.ssl.truststore.password'
    ZOOKEEPER_SSL_TRUSTSTORE_TYPE = 'zookeeper.ssl.truststore.type'
    ZOOKEEPER_SYNC_TIME_MS = 'zookeeper.sync.time.ms'
