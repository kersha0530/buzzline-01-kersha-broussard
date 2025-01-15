import logging
import os
import random

# Ensure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logger Setup for the producer
logging.basicConfig(
    filename="logs/producer_log.log",  # Log file location
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

ADJECTIVES = ["amazing", "funny", "boring", "exciting", "weird"]
ACTIONS = ["found", "saw", "tried", "shared", "loved"]
TOPICS = ["a movie", "a meme", "an app", "a trick", "a story"]

def dynamic_message_generator():
    """Generate dynamic custom messages."""
    for _ in range(5):  # Generate 5 messages
        adjective = random.choice(ADJECTIVES)
        action = random.choice(ACTIONS)
        topic = random.choice(TOPICS)
        message = f"Someone {action} {adjective} {topic}!"
        logging.info(f"Generated: {message}")
        yield message

def main():
    logging.info("Starting the dynamic message generator.")
    for msg in dynamic_message_generator():
        print(msg)
    logging.info("Finished generating messages.")

if __name__ == "__main__":
    main()

