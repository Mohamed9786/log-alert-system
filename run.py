import logging
from monitor.config import Config
from monitor.core import monitor_logs

def setup_logging():
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

def main():
    setup_logging()
    config = Config()
    monitor_logs(config)

if __name__ == "__main__":
    main()
