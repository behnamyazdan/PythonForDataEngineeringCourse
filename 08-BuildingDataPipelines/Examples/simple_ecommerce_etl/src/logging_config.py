# logging_config.py
import logging


class LoggingConfig:
    @staticmethod
    def setup_logging(path):
        # Create handlers
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(path)

        # Set logs levels
        console_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)

        # Create a formatter and set it for handlers
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Configure the root logger
        logging.basicConfig(level=logging.INFO, handlers=[console_handler, file_handler])
