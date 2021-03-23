"""Defines trends calculations for stations"""
import logging

import faust

logger = logging.getLogger(__name__)

INPUT_TOPIC_NAME = "org.chicago.cta.stations"
OUTPUT_TOPIC_NAME = "org.chicago.cta.stations.table.v1"
TABLE_NAME = "stations"

RED_LINE = 'red'
BLUE_LINE = 'blue'
GREEN_LINE = 'green'


# Faust will ingest records from Kafka in this format
class Station(faust.Record):
    stop_id: int
    direction_id: str
    stop_name: str
    station_name: str
    station_descriptive_name: str
    station_id: int
    order: int
    red: bool
    blue: bool
    green: bool


# Faust will produce records to Kafka in this format
class TransformedStation(faust.Record):
    station_id: int
    station_name: str
    order: int
    line: str


# DONE: Define a Faust Stream that ingests data from the Kafka Connect stations topic and
#   places it into a new topic with only the necessary information.
app = faust.App("stations-stream", broker="kafka://localhost:9092", store="memory://")
# DONE: Define the input Kafka Topic. Hint: What topic did Kafka Connect output to?
topic = app.topic(INPUT_TOPIC_NAME, value_type=Station)
# DONE: Define the output Kafka Topic
out_topic = app.topic(OUTPUT_TOPIC_NAME, partitions=1)
# DONE: Define a Faust Table
table = app.Table(
    TABLE_NAME,
    default=TransformedStation,
    partitions=1,
    changelog_topic=out_topic,
)


#
#
# DONE: Using Faust, transform input `Station` records into `TransformedStation` records. Note that
# "line" is the color of the station. So if the `Station` record has the field `red` set to true,
# then you would set the `line` of the `TransformedStation` record to the string `"red"`
#
#
def mapper(station: Station) -> TransformedStation:
    line = RED_LINE if station.red else BLUE_LINE if station.blue else GREEN_LINE
    return TransformedStation(station.station_id, station.station_name, station.order, line)


@app.agent(topic)
async def process_raw_stations(stations):
    stations.add_processor(mapper)
    station: Station
    async for station in stations:
        table[station.station_id] = station


if __name__ == "__main__":
    app.main()
