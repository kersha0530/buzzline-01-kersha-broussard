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

def main() -> None:
    """Main entry point."""
    logger.info("STARTING CONSUMER...")

    # Define the producer's log file
    log_file_path = "logs/producer_log.log"
    logger.info(f"Reading file located at {log_file_path}")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")
        logger.info("Consumer stopped by user.")

    logger.info("CONSUMER ENDED.")

if __name__ == "__main__":
    main()
