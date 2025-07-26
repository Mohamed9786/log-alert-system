from monitor.config import Config

def test_config_loading():
    config = Config("config.yaml")
    assert config.get("log_path") is not None
    assert isinstance(config.email_from, str)
