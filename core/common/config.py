import os

from core.settings.config import AbstractStaticYaml


class Config(AbstractStaticYaml):
    file_absolute_path = r"./core/settings/config.yaml".replace(r'/', os.path.sep)
