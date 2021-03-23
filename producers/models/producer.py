"""Producer base-class providing common utilities and functionality"""
import logging
import time
import socket

from confluent_kafka.admin import AdminClient, NewTopic
from confluent_kafka.avro import AvroProducer
from confluent_kafka.cimpl import KafkaException, KafkaError

from configuration.common_configuration import CommonConfiguration
from configuration.topic_config import TopicConfig
from configuration.cleanup_policy import CleanupPolicy
from configuration.compression_type import CompressionType
from configuration.avro_config import AvroConfig

logger = logging.getLogger(__name__)


class Producer:
    """Defines and provides common functionality amongst Producers"""

    BROKER_URL = "PLAINTEXT://localhost:9092,PLAINTEXT://localhost:9093,PLAINTEXT://localhost:9094"  # "PLAINTEXT://kafka0:9092,PLAINTEXT://kafka1:9093,PLAINTEXT://kafka2:9094"
    SCHEMA_REGISTRY_URL = "http://localhost:8081"  # "http://schema-registry:8081/"

    # Tracks existing topics across all Producer instances
    existing_topics = set([])

    def __init__(
            self,
            topic_name,
            key_schema,
            value_schema=None,
            num_partitions=1,
            num_replicas=1,
    ):
        """Initializes a Producer object with basic settings"""
        self.topic_name = topic_name
        self.key_schema = key_schema
        self.value_schema = value_schema
        self.num_partitions = num_partitions
        self.num_replicas = num_replicas

        #
        #
        # DONE: Configure the broker properties below. Make sure to reference the project README
        # and use the Host URL for Kafka and Schema Registry!
        #
        #
        self.common_broker_properties = {
            # DONE host url for kafka
            CommonConfiguration.BOOTSTRAP_SERVERS.value: self.BROKER_URL,
            # DONE client id
            CommonConfiguration.CLIENT_ID.value: socket.gethostname()
        }

        self.broker_properties = {
            **self.common_broker_properties,
            # DONE schema registry
            AvroConfig.SCHEMA_REGISTRY_URL.value: self.SCHEMA_REGISTRY_URL
        }

        self.adminClient = AdminClient(self.common_broker_properties)

        # If the topic does not already exist, try to create it
        if self.topic_name not in Producer.existing_topics:
            self.create_topic()
            Producer.existing_topics.add(self.topic_name)

        # DONE: Configure the AvroProducer
        self.producer = AvroProducer(
            self.broker_properties,
            self.key_schema,
            self.value_schema
        )

    def create_topic(self):
        """Creates the producer topic if it does not already exist"""
        #
        #
        # DONE: Write code that creates the topic for this producer if it does not already exist on
        # the Kafka Broker.
        #
        #
        topic = NewTopic(
            topic=self.topic_name,
            num_partitions=self.num_partitions,
            replication_factor=self.num_replicas,
            config={
                TopicConfig.CLEANUP_POLICY.value: CleanupPolicy.COMPACT.value,
                CommonConfiguration.COMPRESSION_TYPE.value: CompressionType.LZ4.value,
                TopicConfig.DELETE_RETENTION_MS.value: 100,
                TopicConfig.FILE_DELETE_DELAY_MS.value: 100
            }
        )

        try:
            future_results = self.adminClient.create_topics([topic])
        except Exception as e:
            logger.error(e)

        for topic_name, future_result in future_results.items():
            try:
                future_result.result(timeout=self.time_millis()//1000)
            except KafkaException as exception:
                kafka_error = exception.args[0]
                logger.error(kafka_error)
                # if KafkaError.TOPIC_ALREADY_EXISTS == kafka_error.error_code:
                #     logger.error("Error: topic {} already Exists!".format(topic_name))
            except Exception as e:
                logger.error(e)

    def close(self):
        """Prepares the producer for exit by cleaning up the producer"""
        #
        #
        # DONE: Write cleanup code for the Producer here
        #
        #
        self.producer.flush()

    def time_millis(self):
        """Use this function to get the key for Kafka Events"""
        return int(round(time.time() * 1000))
