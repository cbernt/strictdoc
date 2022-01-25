from typing import Optional

from tomlkit import parse


class SDocConfig:
    def __init__(self, config_dict):
        self.config_dict = config_dict


class ConfigParser:
    @staticmethod
    def parse_config() -> Optional[SDocConfig]:
        with open("strictdoc.toml", "r", encoding="utf8") as config_file:
            config_content = config_file.read()
        config_dict = parse(config_content)
        return SDocConfig(config_dict=config_dict)
