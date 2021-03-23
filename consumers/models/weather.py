"""Contains functionality related to Weather"""
import logging

logger = logging.getLogger(__name__)


class Weather:
    """Defines the Weather model"""

    def __init__(self):
        """Creates the weather model"""
        self.temperature = 70.0
        self.status = "sunny"

    def process_message(self, message):
        """Handles incoming weather data"""
        #
        #
        # DONE: Process incoming weather messages. Set the temperature and status.
        #
        #
        weather_update = message.value()
        self.temperature = weather_update.get("temperature")
        self.status = weather_update.get("status")
        logger.info(f"[Weather] (process_message). Temperature: {self.temperature}. Status: {self.status}")
