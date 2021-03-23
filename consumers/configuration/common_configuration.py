from enum import Enum


class CommonConfiguration(Enum):
    """Kafka Shared Configuration Keys."""

    BOOTSTRAP_SERVERS = 'bootstrap.servers'  # ConsumerConfig, AdminConfig, ProducerConfig
    CLIENT_DNS_LOOKUP = 'client.dns.lookup'  # ConsumerConfig, AdminConfig, ProducerConfig
    CLIENT_ID = 'client.id'  # ConsumerConfig, AdminConfig, ProducerConfig
    COMPRESSION_TYPE = 'compression.type'  # TopicConfig, ProducerConfig, BrokerConfig
    CONNECTIONS_MAX_IDLE_MS = 'connections.max.idle.ms'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    DEFAULT_API_TIMEOUT_MS = 'default.api.timeout.ms'  # ConsumerConfig, AdminConfig
    FETCH_MAX_BYTES = 'fetch.max.bytes'  # ConsumerConfig, BrokerConfig
    INTERCEPTOR_CLASSES = 'interceptor.classes'  # ConsumerConfig, ProducerConfig
    METADATA_MAX_AGE_MS = 'metadata.max.age.ms'  # ConsumerConfig, AdminConfig, ProducerConfig
    METRICS_NUM_SAMPLES = 'metrics.num.samples'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    METRICS_RECORDING_LEVEL = 'metrics.recording.level'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    METRICS_SAMPLE_WINDOW_MS = 'metrics.sample.window.ms'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    METRIC_REPORTERS = 'metric.reporters'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    MIN_INSYNC_REPLICAS = 'min.insync.replicas'  # TopicConfig, BrokerConfig
    RECEIVE_BUFFER_BYTES = 'receive.buffer.bytes'  # ConsumerConfig, AdminConfig, ProducerConfig
    RECONNECT_BACKOFF_MAX_MS = 'reconnect.backoff.max.ms'  # ConsumerConfig, AdminConfig, ProducerConfig
    RECONNECT_BACKOFF_MS = 'reconnect.backoff.ms'  # ConsumerConfig, AdminConfig, ProducerConfig
    REQUEST_TIMEOUT_MS = 'request.timeout.ms'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    RETRIES = 'retries'  # AdminConfig, ProducerConfig
    RETRY_BACKOFF_MS = 'retry.backoff.ms'  # ConsumerConfig, AdminConfig, ProducerConfig
    SASL_CLIENT_CALLBACK_HANDLER_CLASS = 'sasl.client.callback.handler.class'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_JAAS_CONFIG = 'sasl.jaas.config'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_KERBEROS_KINIT_CMD = 'sasl.kerberos.kinit.cmd'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_KERBEROS_MIN_TIME_BEFORE_RELOGIN = 'sasl.kerberos.min.time.before.relogin'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_KERBEROS_SERVICE_NAME = 'sasl.kerberos.service.name'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_KERBEROS_TICKET_RENEW_JITTER = 'sasl.kerberos.ticket.renew.jitter'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_KERBEROS_TICKET_RENEW_WINDOW_FACTOR = 'sasl.kerberos.ticket.renew.window.factor'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_LOGIN_CALLBACK_HANDLER_CLASS = 'sasl.login.callback.handler.class'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_LOGIN_CLASS = 'sasl.login.class'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_LOGIN_REFRESH_BUFFER_SECONDS = 'sasl.login.refresh.buffer.seconds'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_LOGIN_REFRESH_MIN_PERIOD_SECONDS = 'sasl.login.refresh.min.period.seconds'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_LOGIN_REFRESH_WINDOW_FACTOR = 'sasl.login.refresh.window.factor'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_LOGIN_REFRESH_WINDOW_JITTER = 'sasl.login.refresh.window.jitter'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SASL_MECHANISM = 'sasl.mechanism'  # ConsumerConfig, AdminConfig, ProducerConfig
    SECURITY_PROTOCOL = 'security.protocol'  # ConsumerConfig, AdminConfig, ProducerConfig
    SECURITY_PROVIDERS = 'security.providers'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SEND_BUFFER_BYTES = 'send.buffer.bytes'  # ConsumerConfig, AdminConfig, ProducerConfig
    SOCKET_CONNECTION_SETUP_TIMEOUT_MAX_MS = 'socket.connection.setup.timeout.max.ms'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SOCKET_CONNECTION_SETUP_TIMEOUT_MS = 'socket.connection.setup.timeout.ms'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_CIPHER_SUITES = 'ssl.cipher.suites'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_ENABLED_PROTOCOLS = 'ssl.enabled.protocols'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_ENDPOINT_IDENTIFICATION_ALGORITHM = 'ssl.endpoint.identification.algorithm'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_ENGINE_FACTORY_CLASS = 'ssl.engine.factory.class'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_KEYMANAGER_ALGORITHM = 'ssl.keymanager.algorithm'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_KEYSTORE_CERTIFICATE_CHAIN = 'ssl.keystore.certificate.chain'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_KEYSTORE_KEY = 'ssl.keystore.key'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_KEYSTORE_LOCATION = 'ssl.keystore.location'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_KEYSTORE_PASSWORD = 'ssl.keystore.password'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_KEYSTORE_TYPE = 'ssl.keystore_type'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_KEY_PASSWORD = 'ssl.key.password'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_PROTOCOL = 'ssl.protocol'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_PROVIDER = 'ssl.provider'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_SECURE_RANDOM_IMPLEMENTATION = 'ssl.secure.random.implementation'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_TRUSTMANAGER_ALGORITHM = 'ssl.trustmanager.algorithm'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_TRUSTSTORE_CERTIFICATES = 'ssl.truststore.certificates'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_TRUSTSTORE_LOCATION = 'ssl.truststore.location'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_TRUSTSTORE_PASSWORD = 'ssl.truststore.password'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    SSL_TRUSTSTORE_TYPE = 'ssl.truststore.type'  # ConsumerConfig, AdminConfig, ProducerConfig, BrokerConfig
    UNCLEAN_LEADER_ELECTION_ENABLE = 'unclean.leader.election.enable'  # TopicConfig, BrokerConfig
