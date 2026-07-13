from dotenv import load_dotenv
import os
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Loading environment variables...")
load_dotenv()  # take environment variables from .env.


def main():
    if os.getenv("OPENAI_API_KEY") is None:
        logging.info("OPENAI_API_KEY is not set in the environment variables.")
    print("Hello from langchain-course!")


if __name__ == "__main__":
    main()
