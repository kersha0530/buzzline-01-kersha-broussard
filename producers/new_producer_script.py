import os
import time
import logging

# Ensure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logger Setup for the producer
logging.basicConfig(
    log_file_path = "../producers/logs/producer_log.log"
,  # Log file location
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def process_message(log_file_path: str):
    """
    Monitor the log file in real-time and process messages.
    
    Args:
        log_file_path (str): Path to the log file to read.
    """
    if not os.path.exists(log_file_path):
        print(f"Log file not found: {log_file_path}")
        return

    with open(log_file_path, "r") as file:
        # Move to the end of the file to read new entries only
        file.seek(0, os.SEEK_END)
        print(f"Monitoring log file: {log_file_path}")

        while True:
            line = file.readline()
            if not line:
                # Wait for new lines to be written to the file
                time.sleep(1)
                continue

            # Process the new log message
            message = line.strip()
            print(f"Consumed log message: {message}")

            # Analyze the log message
            if "amazing" in message:
                logging.info(f"ALERT: Amazing message detected! {message}")
                print(f"ALERT: Amazing message detected! {message}")

            if "boring" in message:
                logging.warning(f"Notice: Boring message found. {message}")
                print(f"Notice: Boring message found. {message}")

            # Example: Add analytics for specific patterns
            if "tried" in message:
                logging.info(f"Action Analytics: 'Tried' action noted in message. {message}")


def main():
    logging.info("Starting the dynamic message generator.")
    for msg in dynamic_message_generator():
        print(msg)
    logging.info("Finished generating messages.")


if __name__ == "__main__":
    main()

