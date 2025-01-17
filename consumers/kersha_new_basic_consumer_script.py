"""
Kersha's New Basic Consumer Script

Reads a log file as it is being written and processes log messages in real-time.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import time
import logging

#####################################
# Logger Setup for the consumer
#####################################
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/consumer_log_kersha.log",  # Log file location for consumer
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

#####################################
# Define a function to process a single message
#####################################

def process_message(log_file) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        # Move to the end of the file
        file.seek(0, os.SEEK_END)
        print(f"Consumer is ready and waiting for log messages from: {log_file}")

        # Continuous loop to monitor new log entries
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait for new log entries
                continue

            message = line.strip()
            print(f"Consumed log message: {message}")
            logger.info(f"Processed: {message}")

            # Monitor and alert on amazing conditions
            if "amazing" in message.lower():
                print(f"ALERT: Amazing message detected - {message}")
                logger.warning(f"ALERT: Amazing message detected - {message}")

            if "boring" in message.lower():
                print(f"ALERT: Not so exciting message detected - {message}")
                logger.warning(f"ALERT: Not so exciting message detected - {message}")

            if "loved" in message.lower():
                print(f"ALERT: Lovely message detected - {message}")
                logger.warning(f"ALERT: Lovely message detected - {message}")


#####################################
# Define main function for this script
#####################################

def main() -> None:
    """
    Main entry point for the consumer script.
    """
    logger.info("START...")
    log_file_path = "../producers/logs/producer_log.log"  # Adjust this path as needed
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")
    logger.info("END.....")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
