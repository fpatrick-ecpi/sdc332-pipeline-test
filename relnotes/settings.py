"""Read config/settings.env, then config/<APP_ENV>.env on top of it."""
import os
from pathlib import Path

CONFIG_DIR = Path(__file__).resolve().parent.parent / "config"


def _read(path):
    values = {}
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                values[key.strip()] = value.strip()
    return values


def load_settings(app_env=None):
    env = app_env if app_env is not None else os.environ.get("APP_ENV", "")
    settings = _read(CONFIG_DIR / "settings.env")
    if env:
        settings.update(_read(CONFIG_DIR / f"{env}.env"))
    return settings
