"""
Read a log file as it is being written.
"""

import os
import time
import logging

# Set up logger for the consumer
logging.basicConfig(
    filename="../logs/consumer_log_kersha.log",  # Correct relative path from the consumers directory
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

def process_message(log_file: str) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    with open(log_file, "r") as file:
        # Move to the end of the file
        file.seek(0, os.SEEK_END)
        print("Consumer is ready and waiting for a new log message...")

        # Keep running forever
        while True:
            # Read the next line of the file
            line = file.readline()

            # If the line is empty, wait for a new log entry
            if not line:
                time.sleep(1)  # Wait before checking again
                continue

            # Process the new message
            message = line.strip()
            logger.info(f"Consumed message: {message}")
            print(f"Consumed log message: {message}")

            # Check for special conditions in the message
            if "loved amazing" in message:
                print(f"ALERT: Found a favorite message! \n{message}")
                logger.warning(f"ALERT: Found a favorite message! \n{message}")
            elif "boring" in message:
                print(f"NOTE: Found a less exciting message. \n{message}")
                logger.info(f"NOTE: Found a less exciting message. \n{message}")

import os

def main() -> None:
    """Main entry point."""

    logger.info("STARTING CONSUMER...")

    # Define the log file path
    log_file_path = "../producers/logs/producer_log.log"  # Correct relative path

    # Debugging: Print the log file path and current working directory
    print(f"Debug: Log file path being read is: {log_file_path}")
    print(f"Debug: Current working directory is: {os.getcwd()}")

    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        logger.error(f"FileNotFoundError: {e}")
    except KeyboardInterrupt:
        print("User stopped the process.")
        logger.info("Consumer stopped by user.")

    logger.info("CONSUMER ENDED.")


if not os.path.exists(log_file_path):
    raise FileNotFoundError(f"The log file does not exist at: {log_file_path}")

if __name__ == "__main__":
    main()
