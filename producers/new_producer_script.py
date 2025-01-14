import logging

logging.basicConfig(level=logging.INFO)

def main():
    logging.info("This is a new producer script.")

if __name__ == "__main__":
    main()
import logging

# Set up logger
logging.basicConfig(
    filename="logs/producer_log.log",  # Log file location
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def message_generator():
    """A generator that produces custom messages."""
    messages = [
        "Message 1: Custom log message",
        "Message 2: Another custom message",
        "Message 3: Yet another message",
    ]
    for message in messages:
        logging.info(f"Generated: {message}")
        yield message

def main():
    logging.info("Starting the message generator.")
    for msg in message_generator():
        print(msg)
    logging.info("Finished generating messages.")

if __name__ == "__main__":
    main()
