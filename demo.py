from house_price_predictor_mlops.logger import logging
from house_price_predictor_mlops.exception import HousePricePredictorException
import sys

logging.info("This is an info message")
logging.debug("This is a debug message")
logging.warning("This is a warning message")

try:
    # Simulating an error
    x = 1 / 0
except Exception as e:
    raise HousePricePredictorException(e, sys)