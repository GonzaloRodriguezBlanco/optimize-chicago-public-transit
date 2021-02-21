"""Configures a Kafka Connector for Postgres Station data"""
import json
import logging

import requests

logger = logging.getLogger(__name__)

KAFKA_CONNECT_URL = "http://localhost:8083/connectors"
CONNECTOR_NAME = "stations"

CONNECTION_URL = "jdbc:postgresql://postgres:5432/cta"
CONNECTION_USER = "cta_admin"
CONNECTION_PASSWORD = "chicago"
TABLE_WHITELIST = "stations"
MODE = "incrementing"
INCREMENTING_COLUMN_NAME = "stop_id"
TOPIC_PREFIX = "com.udacity."
POLL_INTERVAL_MS = "3600000"


def configure_connector():
    """Starts and configures the Kafka Connect connector"""
    logging.debug("creating or updating kafka connect connector...")

    resp = requests.get(f"{KAFKA_CONNECT_URL}/{CONNECTOR_NAME}")
    if resp.status_code == 200:
        logging.debug("connector already created skipping recreation")
        return

    resp = requests.post(
        KAFKA_CONNECT_URL,
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "name": CONNECTOR_NAME,
            "config": {
                "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
                "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                "key.converter.schemas.enable": "false",
                "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                "value.converter.schemas.enable": "false",
                "batch.max.rows": "500",
                "connection.url": CONNECTION_URL,
                "connection.user": CONNECTION_USER,
                "connection.password": CONNECTION_PASSWORD,
                "table.whitelist": TABLE_WHITELIST,
                "mode": MODE,
                "incrementing.column.name": INCREMENTING_COLUMN_NAME,
                "topic.prefix": TOPIC_PREFIX,
                "poll.interval.ms": POLL_INTERVAL_MS
            }
        }),
    )

    # Ensure a healthy response was given
    resp.raise_for_status()
    logging.debug("connector created successfully")


if __name__ == "__main__":
    configure_connector()
