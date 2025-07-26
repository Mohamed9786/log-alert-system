import os
import yaml
from dotenv import load_dotenv

class Config:
    def __init__(self, config_path="config.yaml"):
        load_dotenv()
        self.defaults = {
            "log_path": "system_errors.log",
            "error_patterns": ["\\[Error\\]", "\\[Warning\\]", "\\[Information\\]"]
        }
        self._load_yaml(config_path)
        self._load_env()

    def _load_yaml(self, path):
        if os.path.exists(path):
            with open(path, "r") as f:
                self.config = yaml.safe_load(f)
        else:
            print(f"⚠️ Config file not found at {path}. Using defaults.")
            self.config = self.defaults

    def _load_env(self):
        self.email_from = os.getenv("EMAIL_FROM")
        self.email_pass = os.getenv("EMAIL_PASS")

    def get(self, key, default=None):
        return self.config.get(key, self.defaults.get(key, default))

    @staticmethod
    def load_config(path="config.yaml"):
        return Config(path)
