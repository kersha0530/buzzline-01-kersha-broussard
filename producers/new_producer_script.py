import logging
import os
import random
import time
import sys

print("Python executable:", sys.executable)
print("Python version:", sys.version)


# Add the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from utils.utils_logger import logger, get_log_file_path

# Ensure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logger Setup for the producer
logging.basicConfig(
    filename="logs/producer_log.log",  # Log file location
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Lists of dynamic content
ADJECTIVES = ["amazing", "funny", "boring", "exciting", "weird"]
ACTIONS = ["found", "saw", "tried", "shared", "loved"]
TOPICS = ["a movie", "a meme", "an app", "a trick", "a story"]

def dynamic_message_generator():
    """Generate dynamic custom messages."""
    while True:  # Run indefinitely
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        message = f"Someone {action} {adjective} {topic}!"
        logging.info(f"Generated: {message}")
        print(message)  # Optional: Display the message in the console
        time.sleep(3)  # Wait for 3 seconds before generating the next message

def main():
    logging.info("Starting the dynamic message generator.")
    try:
        dynamic_message_generator()
    except KeyboardInterrupt:
        logging.info("Stopped the dynamic message generator.")
        print("\nProducer stopped.")

if __name__ == "__main__":
    main()



