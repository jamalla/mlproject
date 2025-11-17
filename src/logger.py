import logging
import os
from datetime import datetime

# Build a timestamped log filename, e.g. "11_17_2025_14_30_00.log"
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Create a logs directory under the current working directory and include
# the timestamped filename in the path. Using a per-run folder keeps logs
# grouped by run and avoids overwriting previous files.
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(logs_path, exist_ok=True)

# Final path to the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the root logger to write INFO+ messages to the file with a
# simple timestamped format. We intentionally don't add handlers here so
# other modules can import `logging` and use the configured root logger.
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    # Example usage: log a test message when run directly
    logging.info("Logger is configured and ready to use.")