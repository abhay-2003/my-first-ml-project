import logging
import os
from datetime import datetime

# Generate log filename with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create logs directory path (not including file name yet)
logs_path = os.path.join(os.getcwd(), "logs")

# Make sure logs directory exists
os.makedirs(logs_path, exist_ok=True)

# Final full path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Set up logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Test logging
if __name__ == "__main__":
    logging.info("Logging has started")
