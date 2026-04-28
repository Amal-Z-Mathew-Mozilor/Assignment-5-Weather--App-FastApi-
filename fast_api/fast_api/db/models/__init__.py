"""fast_api models."""


import pkgutil
from pathlib import Path
from fast_api.db.models.user_model import User
from fast_api.db.models.weather_model import Weather



def load_all_models() -> None:
    """Load all models from this folder."""
    package_dir = Path(__file__).resolve().parent
    modules = pkgutil.walk_packages(
        path=[str(package_dir)],
        prefix="fast_api.db.models.",
    )
    for module in modules:
        __import__(module.name)
